# encoding:utf-8

from django.conf.urls import patterns, include, url
from .views import IndexView

urlpatterns = patterns('',
                       url(r"^$",IndexView.as_view(),name="index")

)