from django.db import models
from reportcard.models import Student
from django.contrib.auth.models import User
from django.contrib import admin
"""
Models to save all emails send to student parents
"""

class Email(models.Model):
    student = models.ForeignKey(Student)
    subject = models.CharField(max_length = 50)
    body = models.CharField("Email message",max_length = 300)
    sent_on = models.DateTimeField(auto_now = True)
    sent_by = models.ForeignKey(User,related_name = "sentby")
    
    def __unicode__(self):
        return self.subject
    
    def get_absolute_url(self):
        return "/report/msgs/email/%s/"  % self.id
    
    class Meta:
        verbose_name_plural= "Email Messages"
    
"""
Model to save all sms sent to student Parent
"""

class Sms(models.Model):
    student= models.ForeignKey(Student)
    body= models.CharField("SMS messages",max_length = 120)
    sent_on = models.DateTimeField(auto_now = True)
    sent_by = models.ForeignKey(User,related_name = "smssender")
    
    def __unicode__(self):
        return self.body[:10]
    
    def get_absolute_url(self):
        return "/report/msgs/sms/%s/" % self.id
    class Meta:
        verbose_name_plural = "SMS Messages"
    



