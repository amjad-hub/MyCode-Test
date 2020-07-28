from django import forms
from .models import Image_M,Image_Dimensions
from django.db import models


class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Image_M
        fields = ('title', 'image','image_url')
                
class Image_DimensionsForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Image_Dimensions
        fields = ('height', 'width')