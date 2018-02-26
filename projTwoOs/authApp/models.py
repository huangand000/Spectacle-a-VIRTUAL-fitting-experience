# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import AbstractUser

import bcrypt

# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=100)
    def check_password(self, raw_password):
        if bcrypt.checkpw(raw_password.encode('utf8'), self.password.encode('utf8')):
            return True
        else:
            return False
