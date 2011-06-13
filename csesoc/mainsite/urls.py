from datetime import datetime

from django.conf.urls.defaults import *

from csesoc.mainsite.models import StreamItem
from csesoc.mainsite.views import streamitem_index

tumblog_dict = {
    'queryset': StreamItem.objects.all(),
    'date_field': 'pub_date',
}

news_dict = {
    'queryset': StreamItem.objects.filter(content_type__name='news item'),
    'date_field': 'pub_date',
}

events_dict = {
    'queryset': StreamItem.objects.filter(content_type__name='event'),
    'date_field': 'pub_date',
}

beta_dict = {
    'queryset': StreamItem.objects.filter(content_type__name='beta'),
    'date_field': 'pub_date',
}

urlpatterns = patterns('django.views.generic.date_based',

    # all news sources
    (r'^$',                                                             streamitem_index, tumblog_dict, 'home'),
    (r'^(?P<year>\d{4})/$',                                             'archive_year',   tumblog_dict, 'home-year'),
    (r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/$',                         'archive_month',  tumblog_dict, 'home-month'),
    (r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/$',        'archive_day',    tumblog_dict, 'home-day'),

    # news
    (r'^news/$',                                                        streamitem_index, news_dict,    'home-news'),
    (r'^news/(?P<year>\d{4})/$',                                        'archive_year',   news_dict,    'home-news-year'),
    (r'^news/(?P<year>\d{4})/(?P<month>[a-z]{3})/$',                    'archive_month',  news_dict,    'home-news-month'),
    (r'^news/(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/$',   'archive_day',    news_dict,    'home-news-day'),

    # events
    (r'^events/$',                                                      streamitem_index, events_dict,  'home-events'),
    (r'^events/(?P<year>\d{4})/$',                                      'archive_year',   events_dict,  'home-events-year'),
    (r'^events/(?P<year>\d{4})/(?P<month>[a-z]{3})/$',                  'archive_month',  events_dict,  'home-events-month'),
    (r'^events/(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/$', 'archive_day',    events_dict,  'home-events-day'),

    # beta (legacy code)
    (r'^beta/$',                                                        streamitem_index, beta_dict,    'home-beta'),
    (r'^beta/(?P<year>\d{4})/$',                                        'archive_year',   beta_dict,    'home-beta-year'),
    (r'^beta/(?P<year>\d{4})/(?P<month>[a-z]{3})/$',                    'archive_month',  beta_dict,    'home-beta-month'),
    (r'^beta/(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/$',   'archive_day',    beta_dict,    'home-beta-day'),

)

