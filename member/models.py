from django.db import models

class Activity(models.Model):
    uact = models.CharField(primary_key=True, max_length=30)
    val = models.FloatField()

class Users(models.Model):
    uuid = models.EmailField(primary_key=True)
    upw = models.CharField(max_length=15)
    uage = models.IntegerField()
    usex = models.CharField(max_length=7)
    uheight = models.FloatField()
    uweight = models.FloatField()
    uact = models.ForeignKey(Activity, on_delete=models.PROTECT)
    urdc = models.FloatField()
