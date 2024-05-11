from django.conf import settings
from rest_framework.views import APIView
from rest_framework import status
from .models import IngestionInformation
from .serializers import IngestionInformationSerializer, ImageUploadForm
from account.models import UserProfile, User
from utils.apihelper import FJR, login_required, get_uuname
import os
from django.core.paginator import Paginator
from datetime import date


class IngestionInformationAPI(APIView):
    def get(self, request):
        pk = request.GET.get("id")
        print(f"{request.user.user_uniq} : {pk}")

        try:
            data = request.user.user_uniq.ingestion_info.get(id=pk)
            result = IngestionInformationSerializer(data).data
            return FJR(msg=f"get {pk} data", data=result)

        except IngestionInformation.DoesNotExist:
            return FJR(error="error", msg="wrong pk value", status=status.HTTP_400_BAD_REQUEST)

    def fetch_file(self, request) -> tuple:
        profile = request.user.user_uniq
        form = ImageUploadForm(request.POST, request.FILES)
        image_path = f"{settings.IMAGE_URI_PREFIX}/default_image.png"
        
        if form.is_valid():
            image = form.cleaned_data["image"]
        else:
            return (image_path, False, "No File")

        suffix = os.path.splitext(image.name)[-1].lower()
        if suffix not in [".gif", ".jpg", ".jpeg", ".bmp", ".png"]:
            return (image_path, False, "invaild format")

        image_name = get_uuname(salt=suffix)

        with open(os.path.join(settings.IMAGE_UPLOAD_DIR, image_name), "wb") as img:
            for chunk in image:
                img.write(chunk)

        save_image_path=f"{settings.IMAGE_URI_PREFIX}/{image_name}"
        return (save_image_path, True, "success")

    def fetch_param(self, request, img_path:tuple):
        profile = request.user.user_uniq
        new_info = IngestionInformation.objects.create(
            userprofile=profile,
            name=request.POST.get("name", "None"),
            calories=request.POST.get("calories", 0),
            carb=request.POST.get("carb", 0),
            protein=request.POST.get("protein", 0),
            fat=request.POST.get("fat", 0),
            natrium=request.POST.get("natrium", 0),
            trans_fat=request.POST.get("trans_fat", 0),
            saturated_fat=request.POST.get("saturated_fat", 0),
            unsaturated_fat=request.POST.get("unsaturated_fat", 0),
            cholesterol=request.POST.get("cholesterol", 0),
            saccharide = request.POST.get("saccharide", 0),
            image_path=img_path[0]
        )
        result = IngestionInformationSerializer(new_info).data
        result = FJR(msg="post data", data=result)
        return result

    @login_required
    def post(self, request):
        img_path = self.fetch_file(request)
        result = self.fetch_param(request, img_path=img_path)

        return result

    def delete(self, request):
        pass

    def put(self, request):
        pass


class IngestionInformationListAPI(APIView):
    def get(self, request):
        page = request.GET.get("page", '1')
        size = request.GET.get("size", '10')
        search_date = request.GET.get("date", None)  # yyyy-nn-dd
        # _search_username = request.GET.get("username", None)
        pk = request.GET.get("id")

        try:
            user = User.objects.get(id=pk)
            query = user.user_uniq.ingestion_info
            if search_date:
                dest_date = date.fromisoformat(search_date)
                data = query.filter(create_time__date=dest_date)
            else:
                data = query.all()

            print(f"length:{len(data)} pagesize:{size} pagenum{page}")
            paginator = Paginator(data.order_by('-pk'), size)
            paged_data = paginator.get_page(page)
            result = IngestionInformationSerializer(paged_data, many=True).data
            result = FJR(msg="get all data", data=result)

        except User.DoesNotExist:
            result = FJR(error="error", msg="invaild User ID", status=status.HTTP_400_BAD_REQUEST)

        # except Exception:
        #     result = FJR(error="error", msg="invaild input Params", status=status.HTTP_400_BAD_REQUEST)

        return result


class IngestionInformationAllListAPI(APIView):
    def get(self, request):
        page = request.GET.get("page", '1')
        size = request.GET.get("size", '10')
        search_date = request.GET.get("date", None)  # yyyy-nn-dd
        data = IngestionInformation.objects.all()
        if search_date:
            search_date = date.fromisoformat(search_date)
            data = data.filter(create_time__date=search_date)
        paginator = Paginator(data.order_by('-pk'), size)
        paged_data = paginator.get_page(page)
        result = IngestionInformationSerializer(paged_data, many=True).data
        result = FJR(msg="get all data", data=result)
        return result


class DailyInformationAPI(APIView):
    def get(self, request):
        pk:int = request.GET.get("id")
        dest_date = request.GET.get("date", None)  # y-m-d

        if dest_date:
            dest_date = date.fromisoformat(dest_date)
        else:
            dest_date = date.today()

        try:
            user = User.objects.get(id=pk)
            data = user.user_uniq.gat_daily_info(dest_date)
            result = FJR(msg=f"{data[1]} total info", data=data[0])

        except User.DoesNotExist:
            result = FJR(error="error", msg="invaild User ID", status=status.HTTP_400_BAD_REQUEST)

        return result
