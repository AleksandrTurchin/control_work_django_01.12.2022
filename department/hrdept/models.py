from django.db import models

# Create your models here.

class hrdept(models.Model):
    department_name = models.CharField(max_length=255)

    def __str__(self):
        return self.department_name

