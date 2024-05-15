from django.db import models
from account.models import UserProfile
from django.conf import settings

### 정규화 필요할까? (Image Table 만들어야하나?)


class IngestionInformation(models.Model):
    """
    테이블 설명

    calories 칼로리 carb 탄수화물 protein 단백질 fat 지방 natrium 나트륨
    """
    userprofile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='ingestion_info')
    create_time = models.DateTimeField(auto_now_add=True, null=True)

    image_path = models.TextField(default=f"{settings.IMAGE_URI_PREFIX}/default_image.png", null=True, blank=True)
    name = models.CharField(default='None', max_length=256, blank=False, null=False)

    ### basic field
    calories = models.DecimalField(default=0, decimal_places=2, max_digits=7)
    carb = models.DecimalField(default=0, decimal_places=2, max_digits=7)         # 탄수화물
    protein = models.DecimalField(default=0, decimal_places=2, max_digits=7)      # 단백질
    fat = models.DecimalField(default=0, decimal_places=2, max_digits=7)          # 지방
    natrium = models.DecimalField(default=0, decimal_places=2, max_digits=7)      # 나트륨
    saccharide = models.DecimalField(default=0, decimal_places=2, max_digits=7)   # 당
    cholesterol = models.DecimalField(default=0, decimal_places=2, max_digits=7)  # 콜레스테롤

    ### advanced field
    trans_fat = models.DecimalField(default=0, decimal_places=2, max_digits=7)
    saturated_fat = models.DecimalField(default=0, decimal_places=2, max_digits=7)
    unsaturated_fat = models.DecimalField(default=0, decimal_places=2, max_digits=7)
