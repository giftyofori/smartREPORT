from django import forms
from django.forms import ModelForm
import datetime
from django.forms.widgets import Select
from models import *

class Emailform(ModelForm):
    class Meta:
        model = Email
        exclude =['student','sent_by']
        widgets = {'subject': forms.TextInput(attrs={"placeholder":"..............Email Subject","style":"width:500px"}),'body': forms.Textarea(attrs={"placeholder":"................Email Body","style":"width:500px"})}
        
class SMSform(ModelForm):
    class Meta:
        model = Sms
        exclude = ['student','sent_by','sent_on']
        widgets = {'body': forms.Textarea(attrs={"placeholder":"SMS cannot br more than 120 words ","style":"width:500px ; height:150px","maxlength":"300"})}