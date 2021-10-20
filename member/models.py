from django.db import models
from django.contrib.auth.models import AbstractUser

class Activity(models.Model):
    uact = models.CharField(primary_key=True, max_length=30)
    val = models.FloatField()

class Users(models.Model):
    uuid = models.EmailField(primary_key=True, verbose_name='이메일')
    upw = models.CharField(max_length=15, verbose_name='비밀번호')
    uage = models.IntegerField(verbose_name='나이')
    SEX_CHOICE = [
        ['F', '여성'],
        ['M', '남성 ']
    ]
    usex = models.CharField(max_length=1, choices=SEX_CHOICE, verbose_name='성별')
    uheight = models.FloatField(verbose_name='키')
    uweight = models.FloatField(verbose_name='몸무게')
    uact = models.ForeignKey(Activity, on_delete=models.PROTECT, verbose_name='활동량')
    urdc = models.FloatField(verbose_name='권장칼로리')
