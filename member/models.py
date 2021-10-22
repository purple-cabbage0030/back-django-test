from django.db import models
from django.contrib.auth.models import AbstractUser

class Activity(models.Model):
    uact = models.CharField(primary_key=True, max_length=30)
    val = models.FloatField()

class Users(models.Model):
    uuid = models.EmailField(primary_key=True, verbose_name='uuid')
    upw = models.CharField(max_length=15, verbose_name='upw')
    uage = models.IntegerField(verbose_name='uage')
    SEX_CHOICE = [
        ['F', '여성'],
        ['M', '남성 ']
    ]
    usex = models.CharField(max_length=1, choices=SEX_CHOICE, verbose_name='usex')
    uheight = models.FloatField(verbose_name='uheight')
    uweight = models.FloatField(verbose_name='uweight')
    uact = models.ForeignKey(Activity, on_delete=models.PROTECT, verbose_name='uact')
    urdc = models.FloatField(verbose_name='urdc')

    def __str__(self):
        return self.uuid