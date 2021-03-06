from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *

from views import *


urlpatterns = patterns('reportcard.views',
	url(r'add/' , 'display_forms'),
	url(r'add_report/', 'add_report'),
	url(r'all/' , 'all_reports'),
	url(r'^detail/(\d+)/$' , 'report_detail'),
        url(r'^error404_sys_me_ot/' , 'error404'),
        url(r'^syserror__me_ot_mtn9','mt9'),
        url(r'^addstudent' , 'add_student'),
        url(r'^student/(\d+)/$' , 'get_student'),
        url(r'^allstudent/(?P<query>.*?)/(?P<course>.*?)/$' ,'all_student'),
        url(r'^getallstudentbyclass/(?P<query>.*?)/(?P<klass>.*?)/$' ,'all_student'),
        url(r'^allstudent/$' ,'all_student'),
        url(r'^asr/(\d+)/$' , 'add_StudentReport'),
        url(r'^vas/(\d+)/$' , 'vas'),
        url(r'^arw/$', 'arwstages'),
        url(r'^changestudent/(?P<id>.*?)/(?P<studentname>.*?)/$','edit_student'),
        url(r'^searchstudent/$','searchstudent'),
        url(r'^arw_main/$','arw_main'),
        url(r'^arwstagtwo/$','arwstagtwo'),
        url(r'^arwstagethree/$','arwstagethree'),
        url(r'^spreadsheet/$','openspreadcenter'),
        url(r'^getspreadsheet/$','getsp'),
        url(r'^computereports/$' ,'compute_reports'),
        #url(r'^posts/(?P<id>\d+)/((?P<showComments>.*)/)?$', 'blog.views.post_detail'),
    

	
    #(r'^poll/(?P<report_key>[^\.^/]+)/$', 'report_detail'),
    #(r'^poll/(?P<report_key>[^\.^/]+)/results/$', 'report_results'),
		
)
