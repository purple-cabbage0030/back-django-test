from django.db import models
from member.models import Users

class Activity(models.Model):
    uact = models.CharField(primary_key=True, max_length=30)
    val = models.FloatField()

class Exercise(models.Model):
    # 운동 종류: 스쿼트, 사이드런지, 사이드레터럴레이즈
    eid = models.IntegerField(primary_key=True, max_length=2)
    ename = models.CharField(max_length=30)
    error_less = models.CharField(max_length=30)
    error_more = models.CharField(max_length=30)

class Train(models.Model):
    # 자동 생성 id를 pk로 사용
    uuid = models.ForeignKey(Users, on_delete=models.CASCADE)
    train_date = models.DateField(auto_now_add=True)
    eid = models.ForeignKey(Exercise, on_delete=models.PROTECT)
    error_name = models.CharField(max_length=30)
    error_count = models.IntegerField(max_length=2)
