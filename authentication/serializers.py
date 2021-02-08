from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.utils.encoding import smart_str, force_str, force_bytes, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode, url_has_allowed_host_and_scheme

from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from sorl_thumbnail_serializer.fields import HyperlinkedSorlImageField
from rest_framework_simplejwt.tokens import RefreshToken, TokenError

import json
from .models import Profile
from .utils import Util

User = get_user_model()

class ProfileSerializer(serializers.ModelSerializer):
    email = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ['full_name', 'email', 'file', 'phone_number', 'dob',]

    def get_email(self, obj):
        return obj.user.email

    # def update(self, instance, validated_data):
        
    #     instance.full_name = validated_data.get('full_name', instance.full_name)
    #     instance.proflie_photo = validated_data.get('file', instance.file)
    #     instance.phone_number = validated_data.get('phone_number', instance.phone_number)
    #     instance.dob = validated_data.get('dob', instance.dob)

    #     return instance

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['profile']

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=68, min_length=8, write_only=True)
    password2 = serializers.CharField(
        required=True, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'password2']

    def validate(self, attrs):
        password = attrs.get('password', '')
        password2 = attrs.get('password2', '')

        if password != password2:
            raise serializers.ValidationError(
            "Password field didn't match.")
        return attrs
    
    def create(self, validated_data):
        validated_data.pop('password2')
        return User.objects.create_user(**validated_data)

class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)
    tokens = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['email', 'password', 'tokens']


    def get_tokens(self, obj):
        user = User.objects.get(email=obj['email'])
        return {'token': user.tokens['access'], 'refresh':user.tokens['refresh']}

    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')

        user = authenticate(email=email, password=password)
        
        if not user:
            raise AuthenticationFailed('Invalid credentials, try again.')
        else:
            if not user.is_active:
                raise AuthenticationFailed('Account disabled, contact admin.')
            else:
                if not user.is_verified:
                    raise AuthenticationFailed('Email not verified.')
        return {
            'id': 0,
            'email': user.email,
            'tokens': self.get_tokens,
        }

class ResendVerification(serializers.Serializer):

    email = serializers.EmailField(max_length=255)

    class Meta:
        fields = ['email']

    def validate(self, attrs):
        email = attrs.get('email', '')
        user = User.objects.filter(email=email)
        if not user.exists():
            raise serializers.ValidationError(
            "You don't have an account.")
        if user.first().is_verified == True:
            raise serializers.ValidationError(
            "Your account has been verified.")
        return attrs

class ResetPasswordEmailRequestSerializer(serializers.Serializer):
    
    email = serializers.EmailField(required=True)

    redirect_url = serializers.CharField(max_length=520, required=False)

    class Meta:
        fields = ['email',]

    def validate(self, attrs):
        email = attrs.get('email', '')
        user = User.objects.filter(email=email)
        if user.exists():
            request = self.context['request']
            user = user.first()
            uidb64 = urlsafe_base64_encode(force_bytes(user.id))
            token = default_token_generator.make_token(user)
            current_site = get_current_site(request).domain
            relativeLink = reverse('authentication:password-reset-confirm', kwargs={'uidb64': uidb64, 'token': token})
            absurl = 'http://' + current_site + relativeLink
            redirect_url = attrs.get('redirect_url', '')
            body = 'Hi,\nUse the link below to reset your password \n' + absurl
            payload = {'body': body, 'subject': 'Reset your password', 'email': user.email} + '?redirect_url=' + redirect_url
            Util.send_email(payload)
            return attrs

        return super().validate(attrs)

class PasswordSerializer(serializers.Serializer):

    password = serializers.CharField(min_length=6, max_length=68, write_only=True)
    token = serializers.CharField(required=True, write_only=True)
    uidb64 = serializers.CharField(required=True, write_only=True)

    class Meta:
        fields = ['passowrd', 'token', 'uidb64']

    def validate(self, attrs):
        try:
            password = attrs.get('password')
            token = attrs.get('token')
            uidb64 = attrs.get('uidb64')

            _id= force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.filter(id=_id).first()
            if not default_token_generator.check_token(user, token):
                raise AuthenticationFailed('The reset link is invalid', 401)
            user.set_password(password)
            user.save()
            return (user)
        except Exception as e:
            raise AuthenticationFailed('The reset link is invalid', 401)
        return super().validate(attrs)

class LogoutSerializer(serializers.Serializer):

    refresh = serializers.CharField()

    default_error_messages = {
        'bad_token': ('Token is expired or invalid.')
    }
    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        
        except TokenError:
            self.fail('bad_token')      

class SocialSerializer(serializers.Serializer):
    """
    Serializer which accepts an OAuth2 access token.
    """
    provider = serializers.CharField(max_length=255, required=True)
    access_token = serializers.CharField(max_length=4096, required=True, trim_whitespace=True)