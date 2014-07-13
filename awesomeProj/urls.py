from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.shortcuts import render_to_response
from django.template.context import Context, RequestContext

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url('^sayhello/', 'blog.views.sayHello'),
                       url(r'^$', 'blog.views.index'),
                       url(r'^(?P<slug>[\w\-]+)/$', 'blog.views.post'),
                       )