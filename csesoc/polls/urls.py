from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('csesoc.polls.views',
    (r'^$', 'index'),
    (r'^(\d+)/vote/$', 'castvote'),
    (r'^(\d+)/results/$', 'results'),
    (r'^(\d+)/processvote/$', 'processvote'),
)
