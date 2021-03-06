__author__ = 'hasmuell'

from django.conf.urls import patterns, url

urlpatterns = patterns('',

                       # pattern: url to a view, view function, reverse name used to dynamically specify urls rather
                       # than hard coding them.
                       url(r'^$', 'stilwiese.views.index', name='home'),
                       url(r'^stilwiese/$', 'stilwiese.views.map', name='stilwiese'),
                       url(r'^blog/$', 'stilwiese.views.blog', name='blog'),
                       url(r'^myFashionbox/$', 'stilwiese.views.fashionbox', name='fashionbox'),
                       url(r'^myCharts/$', 'stilwiese.views.charts', name='charts'),
)

from django.conf.urls import patterns, url