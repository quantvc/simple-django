# encoding:utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'quantvc.views.home', name='home'),
                       url(r'^', include('apps.web.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^accounts/', include('userena.urls')),
                       url(r'^messages/', include('userena.contrib.umessages.urls')),
                       url(r'^auth/', include('allauth.urls')),
                       url(r'^i18n/', include('django.conf.urls.i18n')),
                       url(r'^rosetta/', include('rosetta.urls')),
                       url(r'^django-rq/', include('django_rq.urls')),


)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()




