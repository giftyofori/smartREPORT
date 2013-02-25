from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *



from views import *


urlpatterns = patterns('msgs.views',

    url(r'^email/(\d+)/$' , 'sendemail'),
    url(r'^sms/(\d+)/$' , 'sendsms'),
    #url(r'^msgs/sms/(\d+)/$' , ''),
    #url(r'sendemail/$', 'sndemail'),

)    