__author__ = 'hasmuell'

from django.conf.urls import patterns, url

urlpatterns = patterns('',

                       # pattern: url to a view, view function, reverse name used to dynamically specify urls rather
                       # than hard coding them.
                       url(r'^$', 'stilwiese.views.index', name='home'),
                       url(r'^map/$', 'stilwiese.views.map', name='map'),
                       url(r'^blog/$', 'stilwiese.views.blog', name='blog'),
)

from django.conf.urls import patterns, url