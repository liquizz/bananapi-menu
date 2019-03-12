#from django.db import models
from djongo import models
# Create your models here.

class url(models.Model):
    url_name = models.CharField(max_length = 20)

class pppoe_login(models.Model):
    username = models.CharField(max_length = 25)
    password = models.CharField(max_length = 25)