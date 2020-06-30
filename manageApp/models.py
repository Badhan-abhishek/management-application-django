from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Person(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    email_id = models.CharField(max_length=250, null=True)
    mobile_number = models.CharField(max_length=10, null=True)
    days_attended = models.CharField(max_length=250 , null=True)
    salary = models.IntegerField(null=True)
    def __str__(self):
        return self.name


class PersonData(models.Model):
    name = models.CharField(max_length=250, null=True)
    def __str__(self):
        return self.name
