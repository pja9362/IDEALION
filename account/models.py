from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    lat = models.FloatField(max_length=50, default='37.58219708958901')   #위도
    lng = models.FloatField(max_length=50, default='127.00176613589275')   #경도
    nickname = models.CharField(max_length=100)
    location = models.CharField(max_length=200, default = '0')