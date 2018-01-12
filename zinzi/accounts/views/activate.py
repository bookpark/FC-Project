from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from rest_framework.authtoken.models import Token

from accounts.models import Profile

User = get_user_model()

__all__ = (
    'activate',
)


def activate(request, uidb64=None, token=None):
    uid = force_text(urlsafe_base64_decode(uidb64))
    token = force_text(urlsafe_base64_decode(token))

    user = User.objects.get(pk=uid)

    if token == Token.objects.get(user=user).key:
        user.is_active = True
        user.save()
        Profile.objects.create(user=user)
        return redirect('http://isaccchoi.kr/')
    return redirect('http://isaccchoi.kr/')
