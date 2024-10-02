from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

class Employee(models.Model):

    name = models.CharField(max_length = 100,unique= True)
    description = models.TextField()
    salary = models.DecimalField(max_digits= 10,decimal_places= 2)


    def _str(self):
        return self.name
    

