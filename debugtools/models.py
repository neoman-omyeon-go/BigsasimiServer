from django.db import models


class Blog(models.Model):
    '''테스트용 모델'''
    title = models.CharField(max_length=100)
    body = models.TextField()
    
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    
    class Meta: 
        ordering  =  ['-create_time']
