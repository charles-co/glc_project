import hashlib
from rest_framework.response import Response

from .models import Profile


def auto_logout(*args, **kwargs):
    """Do not compare current user with new one"""
    return {'user': None}


def verify_user(strategy, details, user=None, *args, **kwargs):
    if user:
        if not user.is_verified:
            user.is_verified = True
            strategy.storage.user.changed(user)
    
def save_profile(backend, user, details, response, *args, **kwargs):
    if user:
        try:
            profile = user.profile
        except:
            profile = Profile(user_id=user.id)
            profile.save()
        if profile:
            social_thumb = None
            name = None
            if backend.name == 'facebook' and response.get("picture", {}).get("data", {}).get("url", None) or response.get("name", None):
                social_thumb = response.get("picture", {}).get("data", {}).get("url")
                name = response.get("name", None)
            elif backend.name == 'google-oauth2' and response.get('picture', {}):
                social_thumb = response['picture']
            elif not social_thumb:
                social_thumb = 'http://www.gravatar.com/avatar/'
                social_thumb += hashlib.md5(user.email.lower().encode('utf8')).hexdigest()
                social_thumb += '?size=100'
            if social_thumb or name:
                if social_thumb:
                    profile.social_thumb = social_thumb
                if name:
                    if profile.fulll_name != "Anonymous":
                        profile.full_name = name
                profile.save()

def check_for_email(backend, uid, user=None, *args, **kwargs):
    if not kwargs['details'].get('email'):
        return Response({'error': "Email wasn't provided by oauth provider"}, status=400)