from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import redirect
from django.db.models import QuerySet, Q
from django.http import JsonResponse, HttpResponsePermanentRedirect
from django.shortcuts import get_object_or_404
from django.templatetags.static import static
from django.urls import reverse
from django.utils.encoding import force_str, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, GenericAPIView
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

import jwt
import os
from functools import wraps

from .models import Profile
from .permissions import IsOwner
from .renderers import UserRenderer
from .serializers import (LoginSerializer, ProfileSerializer, RegisterSerializer, 
                            ResetPasswordEmailRequestSerializer, UserSerializer, 
                            PasswordSerializer, LogoutSerializer, ResendVerification)
from .utils import Util

User = get_user_model()

class CustomRedirect(HttpResponsePermanentRedirect):
    allow_schemes=[os.environ.get("APP_SCHEME"), 'http', 'https']

class UserViewSet(GenericViewSet):
    
    renderer_classes = (UserRenderer,)
    queryset = Profile.objects.all()

    def get_queryset(self):
        user = self.request.user
        return super().get_queryset().filter(user=user).select_related('user')

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, user=self.request.user)
        return obj

    # def get_permissions(self):
    #     actions = ['retrieve', 'partial_update', 'update']
    #     if self.action in actions:
    #         return [IsAuthenticated(), IsOwner()]
    #     return super().get_permissions()
         
    def get_serializer_class(self):
        actions = ['register', 'login', 
                    'request_password_reset', 'set_password', 
                    'logout', 'user', 'resend_verification']
        if self.action == actions[0]:
            return RegisterSerializer
        elif self.action == actions[1]:
            return LoginSerializer
        elif self.action == actions[2]:
            return ResetPasswordEmailRequestSerializer
        elif self.action == actions[3]:
            return PasswordSerializer
        elif self.action == actions[4]:
            return LogoutSerializer
        elif self.action == actions[5]:
            return RegisterSerializer
        elif self.action == actions[6]:
            return ResendVerification
        else:
            return ProfileSerializer
        return super().get_serializer_class()

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context

    @action(methods=['post'], detail=False, url_path="resend-verification")
    def resend_verification(self, request):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.send_verification(request, serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @action(methods=['post'], detail=False, url_path="register")
    def register(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        self.send_verification(request, serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def send_verification(self, request, serializer):
        data = serializer.data
        user = User.objects.get(email=data['email'])
        token = RefreshToken.for_user(user)
        current_site = get_current_site(request).domain
        relativeLink = reverse('authentication:authentication:user-verify-email')
        absurl = 'http://' + current_site + relativeLink + "?token=" + str(token)
        body = 'Hi,\nUse the link below to verify your mail \n' + absurl
        payload = {'body': body, 'subject': 'Verify your email', 'email': user.email}
        Util.send_email(payload)

    @action(methods=['post'], detail=False, url_path="verify-email")
    def verify_email(self, request):
        token = request.GET.get('token')
        payload = jwt.decode(token, settings.SECRET_KEY)
        try:
            payload = jwt.decode(token, settings.SECRET_KEY)
            user = User.objects.filter(id=payload['user_id'])
            if not user.first().is_verified:
                user.update(is_verified=True)
            return Response({'email': 'Successfully activated.'}, status=status.HTTP_200_OK)
        except jwt.ExpiredSignatureError as identifier:
            return Response({'error': 'Activation link expired.'}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError as identifier:
            return Response({'error': 'Invalid token.'}, status=status.HTTP_400_BAD_REQUEST)
    
    @action(methods=['post'], detail=False)
    def login(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @action(methods=['post'], detail=False, permission_classes=[IsAuthenticated,])
    def logout(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(methods=['get'], detail=False, url_path="profile", 
    permission_classes=[IsAuthenticated, IsOwner,])
    def profile(self, request):
        profile = self.get_object()
        serializer = self.get_serializer(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)
        # return Response({'error': 'lol'}, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['post'], detail=False, url_path="request-password-reset",)
    def request_password_reset(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response({'success': 'We have sent you a link to reset your password'}, status=status.HTTP_200_OK)

    @action(methods=['patch'], detail=False, url_path="set-password",)
    def set_password(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'success': True, 'message': 'Password reset successful'}, status=status.HTTP_200_OK)

    @action(methods=['put'], detail=False, url_path="profile/update/complete", 
    permission_classes=[IsAuthenticated, IsOwner,], parser_classes=[FormParser, MultiPartParser,])
    def update_profile(self, request, *args, **kwargs):
        
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}
        return Response(serializer.data)
    
    def perform_update(self, serializer):
        serializer.save()

    @action(methods=['patch'], detail=False, url_path="profile/update", 
    permission_classes=[IsAuthenticated, IsOwner,], parser_classes=[FormParser, MultiPartParser,])
    def partial_update_profile(self, request, *args, **kwargs):

        kwargs['partial'] = True
        return self.update_profile(request, *args, **kwargs)

class PasswordResetConfirm(GenericAPIView):

    def get(self, request, uidb64, token):
        redirect_url = request.GET.get('redirect_url')
        try:
            _id = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.filter(id=_id).first()
        
            if not default_token_generator.check_token(user, token):
                if len(redirect_url) > 3:
                    return CustomRedirect(redirect_url + '?token_valid=False')
                else:
                    return CustomRedirect(os.environ.get("FRONTEND_URL","") + '?token_valid=False')
            if redirect_url and len(redirect_url) > 3:    
                return CustomRedirect(redirect_url + "?token_valid=True&message=Credentials valid&uidb64="+uid64+"&token="+token)
            return CustomRedirect(os.environ.get("FRONTEND_URL","") + "?token_valid=True&message=Credentials valid&uidb64="+uid64+"&token="+token)
        except DjangoUnicodeDecodeError:
            return CustomRedirect(redirect_url + '?token_valid=False')

