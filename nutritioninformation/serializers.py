from rest_framework import serializers
from .models import IngestionInformation
from django import forms


class IngestionInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = IngestionInformation
        fields = '__all__'


class ImageUploadForm(forms.Form):
    image = forms.FileField()
    name = forms.CharField()
    # etc...
