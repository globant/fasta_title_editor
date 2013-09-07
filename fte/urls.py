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
	#url(r'^articles/2003/$', 'news.views.special_case_2003'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
