from django.conf.urls.defaults import patterns, include, url

from fte_main import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    ##url(r'^fte/', 'fte.views.home', name='home'),
    url(r'^$', include('fte_main.urls')),
    url(r'^result/$', views.index, name='result'),
    url(r'^download/(?P<download_file>.+)$', 
    	views.downloadstatic, name='download'),
)
