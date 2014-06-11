__author__ = 'hasmuell'

from django.conf.urls import patterns, url

urlpatterns = patterns('',

                       # pattern: url to a view, view function, reverse name used to dynamically specify urls rather
                       # than hard coding them.
                       url(r'^$', 'stilwiese.views.index', name='home'),
)