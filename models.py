from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class groupdata(models.Model):
    branch=models.CharField(max_length=20)

    # def __str__(self):
    #     return self.Id
class StudentData(models.Model):
    # user=models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    email = models.EmailField()
    address = models.CharField(max_length=30)
    gender = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    group=models.ForeignKey(groupdata,on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.Id

