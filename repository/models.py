from django.db import models
from member.models import Users

class Exercise(models.Model):
    eid = models.IntegerField(primary_key=True)
    ename = models.CharField(max_length=30)
    error_name = models.CharField(max_length=30)

class Train(models.Model):
    train_id = models.AutoField(primary_key=True)
    uuid = models.ForeignKey(Users, on_delete=models.CASCADE)
    train_date = models.DateField(auto_now_add=True)
    eid = models.ForeignKey(Exercise, on_delete=models.PROTECT)
    error_name = models.CharField(max_length=30)
    count = models.IntegerField()
    error_count = models.IntegerField()

class Food(models.Model):
    fid = models.CharField(primary_key=True, max_length=20)
    fname = models.CharField(max_length=30)
    famount = models.IntegerField()
    fcal = models.FloatField()
    fcarboh = models.FloatField()
    fprotein = models.FloatField()
    ffat = models.FloatField()

    def __str__(self):
        return f"{self.fid}. {self.fname}"

    class Meta:
        ordering=['fname']

class Diet(models.Model):
    diet_id = models.AutoField(primary_key=True)
    uuid = models.ForeignKey(Users, on_delete=models.CASCADE)
    diet_datetime = models.DateTimeField(auto_now_add=True)
    meal = models.CharField(max_length=30)
    fid = models.ForeignKey(Food, on_delete=models.PROTECT)
    fname = models.CharField(max_length=30)
    amount = models.IntegerField()
    cal = models.FloatField()
    carboh = models.FloatField()
    protein = models.FloatField()
    fat = models.FloatField()    
