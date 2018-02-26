# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=100)
<<<<<<< HEAD
=======
    def check_password(self, raw_password):
        if self.password == raw_password:
            return True
        else:
            return False
>>>>>>> 80fb587b1e805b684a3915d0730670f8c45a2640
