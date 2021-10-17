from django.db import models
from member.models import Users

class Food(models.Model):
    fid = models.CharField(primary_key=True, max_length=20)
    fname = models.CharField(max_length=30)
    famount = models.IntegerField(max_length=10)
    fcal = models.FloatField()
    fcarboh = models.FloatField()
    fprotein = models.FloatField()
    ffat = models.FloatField()

class Diet(models.Model):
    # 자동 생성 id를 pk로 사용
    uuid = models.ForeignKey(Users, on_delete=models.CASCADE)
    diet_datetime = models.DateTimeField()
    meal = models.CharField(max_length=30)
    fid = models.ForeignKey(Food, on_delete=models.PROTECT)
    fname = models.CharField(max_length=30)
    amount = models.IntegerField(max_length=10)
    cal = models.FloatField()
    carboh = models.FloatField()
    protein = models.FloatField()
    fat = models.FloatField()    
