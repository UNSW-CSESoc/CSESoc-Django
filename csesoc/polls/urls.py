from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('polls.views',
    (r'^vote/(\d+)$', 'castvote'),
    (r'^vote/(\d+)/(error)$', 'castvote'),
    (r'^results/(\d+)$', 'results'),
    (r'^processvote/(\d+)$', 'processvote'),
)
