from django import forms

from django.contrib.auth import get_user_model

from models import *

class UploadSnapshotForm(forms.Form):
    file = forms.FileField()