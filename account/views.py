from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer, UserLoginSerializer
from rest_framework.views import APIView
from django.http import JsonResponse
import jwt
from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from rest_framework import status
from config.settings.base import SECRET_KEY

from utils.apihelper import FormatResponse

# model
from .models import User


class UserRegister(APIView):
    def post(self, request):
        print("Register Info : ",request.data)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(FormatResponse(data=serializer.data))

        if serializer.errors.get("username", None):
            return JsonResponse(FormatResponse(msg="id already exists",),status=status.HTTP_400_BAD_REQUEST)

        return JsonResponse(FormatResponse(error="error",
                                           msg=serializer.error_messages,
                                           data=serializer.errors),
                            status=status.HTTP_400_BAD_REQUEST)


class UserLogin(APIView):
    # 유저 정보 확인
    def get(self, request):
        try:
            # access token을 decode 해서 유저 id 추출 => 유저 식별
            access_token = request.COOKIES['access']
            payload = jwt.decode(access_token, SECRET_KEY, algorithms=['HS256'])
            pk = payload.get('user_id')
            user = User.objects.get(pk=pk)
            serializer = UserSerializer(instance=user)
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)

        except (jwt.exceptions.ExpiredSignatureError):
            # 토큰 만료 시 토큰 갱신
            serializer = TokenRefreshSerializer(data={'refresh': request.COOKIES.get('refresh', None)})
            try:
                if serializer.is_valid(raise_exception=True):
                    token = serializer.validated_data
                    access = token['access']
                    payload = jwt.decode(access, SECRET_KEY, algorithms=['HS256'])
                    pk = payload.get('user_id')
                    user = User.objects.get(id=pk)
                    serializer = UserSerializer(user)
                    result = {"msg":"토큰 재발급 완료", "user":serializer.data}
                    res = JsonResponse(FormatResponse(msg="token is refreshed",data=result))
                    res.set_cookie('access', access, httponly=True)
                    return res

            except Exception as e:
                print(e)
                raise jwt.exceptions.InvalidTokenError

        except (jwt.exceptions.InvalidTokenError):
            # 사용 불가능한 토큰일 때
            return JsonResponse(FormatResponse(error="error", msg="invaild token"), status=status.HTTP_400_BAD_REQUEST)

        except Exception:
            return JsonResponse(FormatResponse(error="error", msg="is not contain token"), status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        user = serializer.authenticate_user()

        if user:
            refresh = RefreshToken.for_user(user=user)
            response = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
            result = JsonResponse(FormatResponse(msg="Login success",data=response))
            result.set_cookie("access", response["access"], httponly=True)
            result.set_cookie("refresh", response["refresh"], httponly=True)
            return result
        else:
            return JsonResponse(FormatResponse(error="error", msg="user miss match"), status=status.HTTP_400_BAD_REQUEST)


class UserLogout(APIView):
    def get(self, request):
        response = JsonResponse(FormatResponse(msg="프론트에서 토큰 삭제 하세용~"))
        response.delete_cookie("access")
        response.delete_cookie("refresh")
        return response
