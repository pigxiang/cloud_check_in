from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Account(models.Model):
    user = models.OneToOneField(User)
    oa_name = models.CharField(max_length=32)
    oa_password = models.CharField(max_length=32)