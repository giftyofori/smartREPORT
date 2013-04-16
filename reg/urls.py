from django.conf.urls import patterns, include, url
from models import *
from views import *
from django.conf.urls.defaults import *


urlpatterns = patterns('reg.views',
	url(r'^home/', 'main',),
	url(r"^profile/(\d+)/$", "profile"),
	url(r'^logged/', 'logged'),
)
