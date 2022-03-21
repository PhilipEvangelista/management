from django.db import models
from django.utils import timezone
# Create your models here.


class Name(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Information(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
    date = models.DateTimeField(default=timezone.now)
    interest = models.FloatField(default=0)
    balance = models.FloatField(default=0)
    interest_bool = models.BooleanField(default=True)
    agreement = models.BooleanField(default=False)
    date_debts = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Security(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.username
