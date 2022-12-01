from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=255)
    post = models.CharField(max_length=255)
    salary = models.DecimalField(max_digits=8, decimal_places=2)
    department = models.CharField(max_length=255)



