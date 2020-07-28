from django.db import models
from django.core.files import File
from urllib.request import urlopen
from tempfile import NamedTemporaryFile
import os
import urllib.request
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponse


class Image_M(models.Model):
    title = models.CharField(max_length=200)
    height = models.PositiveIntegerField(default=350)
    width = models.PositiveIntegerField(default=350)
    image = models.ImageField(upload_to='images',blank = 'true')
    image_url = models.URLField(max_length=200,blank = 'true')
#    image = models.ImageField(upload_to='images',blank = 'true')
    def save(self, *args, **kwargs):
        if self.image_url and not self.image:
            img_temp = NamedTemporaryFile(delete=True)
            img_temp.write(urlopen(self.image_url).read())
            img_temp.flush()
            self.image.save(f"image_{self.pk}.jpg", File(img_temp))
        super(Image_M, self).save(*args, **kwargs)

        
    def get_absolute_url(self):
        return reverse("image-title",kwargs={"image_title":self.title})
        
class Image_Dimensions(models.Model):
    height = models.PositiveIntegerField(default=50)
    width = models.PositiveIntegerField(default=50)

