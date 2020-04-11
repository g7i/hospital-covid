from django.contrib.auth.models import User
from django.db import models


class Hospital(models.Model):
    name = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    district = models.CharField(max_length=100)
    code = models.IntegerField()
    key = models.CharField(max_length=50)
    state = models.CharField(max_length=70)
    contact = models.CharField(max_length=20)
    address = models.TextField()
    type = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    report = models.FileField()
    sample = models.IntegerField()
    positive = models.IntegerField()
    negative = models.IntegerField()
    admit = models.IntegerField()
    pending = models.IntegerField()
    deaths = models.IntegerField()
    discharged = models.IntegerField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username + f' : {self.date}'


class Patient(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    father = models.CharField(max_length=100)
    aadhar = models.BigIntegerField()
    mobile = models.BigIntegerField()
    status = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    come_by = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.aadhar} : ' + self.name
