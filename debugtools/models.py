from django.db import models


class Blog(models.Model):
    '''테스트용 모델'''
    title = models.CharField(max_length=100)
    body = models.TextField()
