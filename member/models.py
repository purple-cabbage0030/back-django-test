from django.db import models
from train.models import Activity

class Users(models.Model):
    uuid = models.EmailField(primary_key=True)
    upw = models.CharField(max_length=15)
    uage = models.IntegerField(max_length=3)
    usex = models.CharField(max_length=7)
    uheight = models.FloatField()
    uweight = models.FloatField()
    uact = models.ForeignKey(Activity, on_delete=models.PROTECT)
    urdc = models.FloatField()
