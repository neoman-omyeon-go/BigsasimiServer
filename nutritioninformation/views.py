from django.conf import settings
from rest_framework.views import APIView
from rest_framework import status
from .models import IngestionInformation
from .serializers import IngestionInformationSerializer, ImageUploadForm
from account.models import UserProfile
from utils.apihelper import FJR, login_required, get_uuname
import os
from account.models import User

class IngestionInformationAPI(APIView):
    def get(self, request):
        data = request.user.user_uniq.ingestion_info
        print(request.user.user_uniq)
        result = IngestionInformationSerializer(data, many=True).data
        return FJR(msg="get all data", data=result)
    
    def post(self, request):
        profile = request.user.user_uniq
        form = ImageUploadForm(request.POST, request.FILES)
        
        if form.is_valid():
            image = form.cleaned_data["image"]
            name = form.cleaned_data["name"]
        else:
            return FJR(error="error", msg="invaild data", status=status.HTTP_400_BAD_REQUEST)
        
        suffix = os.path.splitext(image.name)[-1].lower()
        if suffix not in [".gif", ".jpg", ".jpeg", ".bmp", ".png"]:
            return FJR(error="error", msg="invaild format", status=status.HTTP_400_BAD_REQUEST)
        
        image_name = get_uuname(salt=suffix)
        
        with open(os.path.join(settings.IMAGE_UPLOAD_DIR, image_name), "wb") as img:
            for chunk in image:
                img.write(chunk)
        
        # 추가 정보 기입 해야함...
        new_info = IngestionInformation.objects.create(
            userprofile=profile,
            image_path=f"{settings.IMAGE_URI_PREFIX}/{image_name}",
            name=name
        )
        
        result = IngestionInformationSerializer(new_info).data
        return FJR(msg="get all data", data=result)
