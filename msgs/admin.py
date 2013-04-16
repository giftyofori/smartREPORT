from django.contrib import admin
from models import *
"""
Adminstaration Customization
"""

class EmailAdmin(admin.ModelAdmin):
    list_display = ['student' , 'subject' , 'body','sent_on' , 'sent_by']
    list_filter = ["sent_on",]
class SmsAdmin(admin.ModelAdmin):
    list_display = ['student' ,'body','sent_on' , 'sent_by']
    list_filter = ["sent_on",]
    

admin.site.register(Email,EmailAdmin)
admin.site.register(Sms,SmsAdmin)
