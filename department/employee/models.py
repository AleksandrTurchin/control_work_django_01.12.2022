from django.db import models
# import Hrdept

class Employee(models.Model):
    name = models.CharField(max_length=255)
    post = models.CharField(max_length=255)
    salary = models.DecimalField(max_digits=8, decimal_places=2)
    department = models.ForeignKey(Hrdept, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name


class Hrdept(models.Model):
    department_name = models.CharField(max_length=255)

    def __str__(self):
        return self.department_name
