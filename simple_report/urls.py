from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *
from views import *


urlpatterns = patterns('simple_report.views',
    url(r'^$', 'recent'),
    url(r'^create/$', 'add_report'), 
	url(r'^detail/(\d+)/$' , 'detail'),
	url(r'^send/(\d+)/$' , 'send_report'),
	url(r'^create2/$' , 'add_report_main'),

	
    #(r'^poll/(?P<report_key>[^\.^/]+)/$', 'report_detail'),
    #(r'^poll/(?P<report_key>[^\.^/]+)/results/$', 'report_results'),	
)
