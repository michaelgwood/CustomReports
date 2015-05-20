from django.conf.urls import patterns, url, include
from django.views.generic import TemplateView

import tables

from . import views

urlpatterns = patterns('',

    url(r'^$', 'charts.views.index', name='index'),
    url(r'^dashboard$', 'charts.views.dashboard', name='dashboard'),
    url(r'^testrun/(?P<id>[0-9]+)$', 'charts.views.testrun', name='testrun'),
    url(r'^testrun/$', lambda x: HttpResponseBadRequest(), name='base_testrun'),
    url(r'^tableexample/$', TemplateView.as_view(template_name="charts/exampletablepage.html"), {'table_name': "charts:"+tables.TestPlanTable.__name__.lower()}),
    url(r'^xhr_tables/', include('charts.tables')),

)
