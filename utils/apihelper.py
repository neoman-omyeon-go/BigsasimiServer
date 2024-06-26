import functools
from django.utils.crypto import get_random_string
import os
from django.conf import settings

# http
from rest_framework import status
from django.http import JsonResponse

from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


def get_uuname(salt:str="") -> str:
    uuname = get_random_string(32, allowed_chars="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789") + salt
    while os.path.exists(os.path.join(settings.IMAGE_UPLOAD_DIR, uuname)):
        uuname = get_random_string(32, allowed_chars="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789") + salt

    return uuname


def validate_serializer(serializer):
    '''data checker'''
    def validate(view_method):
        @functools.wraps(view_method)
        def handle(*args, **kwargs):
            self = args[0]
            request = args[1]
            seri = serializer(data=request.data)
            if seri.is_valid():
                request.data = seri.data
                request.serializer = seri
                return view_method(*args, **kwargs)
            else:
                return self.invalid_serializer(seri)

        return handle

    return validate


def FormatResponse(error:str=None, msg:str=None, data:dict=None) -> dict:
    return {"error": error, "msg":msg, "data": data}


def FJR(error:str=None, msg:str=None, data:dict=None, status=status.HTTP_200_OK):
    """Formatting Json Response"""
    r = {"error": error, "msg":msg, "data": data}
    return JsonResponse(r, status=status)


class BasePermissionDecorator(object):
    def __init__(self, func):
        self.func = func

    def __get__(self, obj, obj_type):
        return functools.partial(self.__call__, obj)

    def error(self, msg):
        return FJR(error="permission-denied", msg=msg, status=status.HTTP_400_BAD_REQUEST)

    def __call__(self, *args, **kwargs):
        self.request = args[1]
        if self.check_permission():
            if not self.request.user.is_active:
                return self.error("Your account is disabled")
            return self.func(*args, **kwargs)
        else:
            return self.error("Please login first")

    def check_permission(self):
        raise NotImplementedError()


class login_required(BasePermissionDecorator):
    """
    jwt라 헤더검증 자동으로함
    명시적 표시로 사용 가능...
    """
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def check_permission(self):
        return self.request.user.is_authenticated
