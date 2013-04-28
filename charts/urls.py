from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *



from views import *


urlpatterns = patterns('charts.views',
    url(r'^draw/$' , 'draw'),
    url(r'^base/$','home'),
    url(r'^piechart/$','piechart'),
    url(r'^barchart/$','barchart'),
    url(r'^CSAS/((?P<term>.*)/)?$' ,'CSAS'),
    url(r'^POC/$' ,'POC'),


)    