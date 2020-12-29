from django.db import models
from django.contrib.auth.models import User
# Create your models here.
'''

class Wrokers(models.Model):
    name = models.CharField(max_length = 255)
    email = models.EmailField(unique=True,max_length=255)
    username = models.CharField(max_length = 255)
    role = models.CharField(max_length = 255)

    '''
