from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from django.http import JsonResponse
import jwt
from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from rest_framework import status
from config.settings.base import SECRET_KEY
import os
from django.conf import settings

# model
from .models import User

# ser
from .serializers import UserSerializer, UserLoginSerializer, UserProfileSerializer, EditUserProfileSerializer, ImageUploadSerializer

# etc...
from utils.apihelper import FormatResponse, FJR, login_required, get_uuname


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


class UserProfileAPI(APIView):
    def get(self, request):
        id = request.GET.get("id")
        username = request.GET.get("username")
        try:
            if id:
                u = User.objects.get(id=id).user_uniq
                ser = UserProfileSerializer(u)
            elif username:
                u = User.objects.get(username=username).user_uniq
                ser = UserProfileSerializer(u)
            else:
                result = FJR(error="error", msg="params error", status=status.HTTP_400_BAD_REQUEST)
            result = FJR(data=ser.data)

        except User.DoesNotExist:
            result = FJR(error="error", msg="user not exist",status=status.HTTP_400_BAD_REQUEST)

        return result

    @login_required
    def post(self, request):
        key = request.POST.get('key', None)
        value = request.POST.get('value', None)

        if key is not None and value is not None:
            user_profile = request.user.user_uniq
            setattr(user_profile, key, value)
            user_profile.save()
            return FJR(msg="user profile changed", data=UserProfileSerializer(user_profile).data)

        result = FJR(error="error", msg="params error",status=status.HTTP_400_BAD_REQUEST)
        return result

    @login_required
    def put(self, request):
        def reform_list(arr:list) -> list:
            result = list()
            for i in set(arr):
                if len(i) != 0:
                    result.append(i)
            return sorted(result)

        print("request : ", request)
        print("Post : ", request.POST)

        serializer = EditUserProfileSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            data = serializer.validated_data
            user_profile = request.user.user_uniq
            disease_is_none = data.get("disease",None)
            allergy_is_none = data.get("allergy",None)

            if disease_is_none is None:
                data["disease"] = list()
            else:
                data["disease"] = reform_list(data["disease"].split(","))

            if allergy_is_none is None:
                data["allergy"] = list()
            else:
                data["allergy"] = reform_list(data["allergy"].split(","))

            for k, v in data.items():
                setattr(user_profile, k, v)
            user_profile.save()
            return FJR(msg="user profile changed", data=UserProfileSerializer(user_profile).data)
        else:
            return FJR(error="error", msg="invalid access")


class UserProfileAddAPI(APIView):
    @login_required
    def get(self, request):
        user = request.user
        userprofile = user.user_uniq
        target = request.GET.get('target',None)

        if target in ["disease", "allergy", "medicine"]:
            value = request.GET.get('value',None)
            if value is None:
                return FJR(error="error", msg="need value params")
        else:
            return FJR(error="error", msg="invaild target params")

        if target == "disease":
            userprofile.disease.append(value)
            userprofile.disease.sort()
        elif target == "allergy":
            userprofile.allergy.append(value)
            userprofile.allergy.sort()
        elif target == "medicine":
            userprofile.medicine.append(value)
            userprofile.medicine.sort()
        else:
            return FJR(error="error", msg="invaild target params")
        userprofile.save()

        return FJR(msg="user profile changed", data=UserProfileSerializer(userprofile).data)


class UserProfileRemoveAPI(APIView):
    @login_required
    def get(self, request):
        user = request.user
        userprofile = user.user_uniq
        target = request.GET.get('target',None)

        if target in ["disease", "allergy", "medicine"]:
            value = request.GET.get('value',None)
            if value is None:
                return FJR(error="error", msg="need value params")
        else:
            return FJR(error="error", msg="invaild target params")

        ### 인덱스로 서치할지 값으로 서치할지는 보류... 지금은 값으로
        try:
            if target == "disease":
                idx = userprofile.disease.index(value)
                del userprofile.disease[idx]
                userprofile.disease.sort()
            elif target == "allergy":
                idx = userprofile.allergy.index(value)
                del userprofile.allergy[idx]
                userprofile.allergy.sort()
            elif target == "medicine":
                idx = userprofile.medicine.index(value)
                del userprofile.medicine[idx]
                userprofile.medicine.sort()
            else:
                return FJR(error="error", msg="invaild target params")
            userprofile.save()
            return FJR(msg="user profile changed", data=UserProfileSerializer(userprofile).data)

        except ValueError:
            return FJR(error="error", msg="value not found")


class UserProfileAvatarUpload(APIView):
    def post(self, request):
        user_profile = request.user.user_uniq
        serializer = ImageUploadSerializer(data=request.data)

        if serializer.is_valid():
            image = serializer.validated_data.get('image', None)
        else:
            return FJR(error="error", msg="invalid image file")

        # 이미지 저장
        suffix = os.path.splitext(image.name)[-1].lower()
        if suffix not in [".gif", ".jpg", ".jpeg", ".bmp", ".png"]:
            return FJR(error="error", msg="invalid file format")
        image_name = get_uuname(salt=suffix)
        with open(os.path.join(settings.AVATAR_UPLOAD_DIR, image_name), "wb") as img:
            for chunk in image:
                img.write(chunk)

        # 이전 이미지파일 파일 삭제
        try:
            before_avatar_URI = user_profile.avatar
            if before_avatar_URI != settings.DEFAULT_AVATAR_URI:
                target_path = f"{settings.BASE_DIR}{before_avatar_URI}"
                os.remove(target_path)
            else:
                print("can't remove Default Image")
                pass
        except OSError as e:
            print("OSError: ", target_path, e.strerror)
        finally:
            current_avatar_path = f"{settings.AVATAR_URI_PREFIX}/{image_name}"
            user_profile.avatar = current_avatar_path
            user_profile.save()

        return FJR(msg="avatar changed", data={"avatar":current_avatar_path})
