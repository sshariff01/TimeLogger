from django.conf.urls import patterns, include, url
from django.contrib import admin

from logs import views

urlpatterns = patterns('',
    url(r'^$', 'logs.views.home', name='home'),
    url(r'^record/', 'logs.views.record', name='record'),

    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
