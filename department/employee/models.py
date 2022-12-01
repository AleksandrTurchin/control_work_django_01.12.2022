from django.db import models
from hrdept import hrdept

class Employee(models.Model):
    name = models.CharField(max_length=255)
    post = models.CharField(max_length=255)
    salary = models.DecimalField(max_digits=8, decimal_places=2)
    department = models.ForeignKey(hrdept, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name



