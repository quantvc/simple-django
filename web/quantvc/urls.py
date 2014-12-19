from django.conf.urls import patterns, include, url
from django.contrib import admin


from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'quantvc.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^grappelli/', include('grappelli.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^accounts/', include('userena.urls')),
                       url(r'^messages/', include('userena.contrib.umessages.urls')),
                       # url(r'^accounts/', include('allauth.urls')),
                       url(r'^i18n/', include('django.conf.urls.i18n')),

)


