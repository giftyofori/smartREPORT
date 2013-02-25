from django.forms import ModelForm
from django import forms
from reg import models

class ProfileForm(ModelForm):
    class Meta:
        model = models.UserProfile
        exclude = ["logins", "user"]