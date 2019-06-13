from django.db import models

class Employee(models.Model):
    id_no = models.IntegerField()
    name = models.CharField(max_length=50)
    salary = models.FloatField()
    location = models.CharField(max_length=50)
