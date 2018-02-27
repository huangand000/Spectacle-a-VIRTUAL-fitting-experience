# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.

class Glasses(models.Model):
    name = models.CharField(max_length=255)
    route = models.CharField(max_length=255)

class Snapshot(models.Model):
    file_upload = models.FileField(upload_to='static/snapshots')
    user = models.ForeignKey(User, related_name='snapshots')