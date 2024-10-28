from django.db import models

# Create your models here.

class Registeration(models.Model):

    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    phone_number = models.DecimalField(max_digits=11, decimal_places=0)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    DOB = models.DateField(null=False)


class Register(models.Model):

    phone_number = models.DecimalField(max_digits=11, decimal_places=0)
    mobile_network = models.CharField(max_length=25)





