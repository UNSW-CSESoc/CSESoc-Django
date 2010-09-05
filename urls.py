from datetime import datetime

from django.conf.urls.defaults import *
from django.contrib import admin

from csesoc import settings
from csesoc.campattendees.views import signup
from csesoc.campleaders.views import apply
from csesoc.game.views import game_scores, game_static, game_static_latest
from csesoc.mainsite.views import static, thedate
from csesoc.scheduler.views import join, results
<<<<<<< HEAD
from csesoc.sponsors.views import sponsors
from csesoc.suggestions.views import suggest
from csesoc.posts.views import recentPosts

admin.autodiscover()

tumblog_dict = {
      'queryset': mainsite.models.StreamItem.objects.all(),
      'date_field': 'pub_date',
      }

news_dict = {
      'queryset': mainsite.models.StreamItem.objects.filter(content_type__name='news item'),
      'date_field': 'pub_date',
      }

events_dict = {
      'queryset': mainsite.models.StreamItem.objects.filter(content_type__name='event'),
      'date_field': 'pub_date',
      }

beta_dict = {
      'queryset': mainsite.models.StreamItem.objects.filter(content_type__name='beta'),
      'date_field': 'pub_date',
      }

urlpatterns = patterns(
      '',
      (r'static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_URL}),
      # Admin site
      (r'^admin/(.*)', 'csesoc.auth.backends.admin_wrapper'),
      # Login redirect
      (r'accounts/login/$', 'csesoc.auth.backends.cse_login'),

      #News || News -> Recent News
      (r'^news/recent/$', recentPosts),
      (r'^news/recent/p(?P<offset>\d+)/$', recentPosts),

      # Sponsors
      (r'^oursponsors/$', sponsors),
)

urlpatterns += patterns(
      'django.views.generic.date_based',
      # all news sources
      (r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/$',               'archive_day',   tumblog_dict),
      (r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/$',                                'archive_month', tumblog_dict),
      (r'^(?P<year>\d{4})/$',                                                    'archive_year',  tumblog_dict),
      (r'^$', 'archive_index', tumblog_dict, "home"),

      # events
      (r'^events/(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/$',               'archive_day',   events_dict),
      (r'^events/(?P<year>\d{4})/(?P<month>[a-z]{3})/$',                                'archive_month', events_dict),
      (r'^events/(?P<year>\d{4})/$',                                                    'archive_year',  events_dict),
      (r'^events/$', 'archive_index', events_dict, "home-events"),

      # beta
      (r'^beta/(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/$',               'archive_day',   beta_dict),
      (r'^beta/(?P<year>\d{4})/(?P<month>[a-z]{3})/$',                                'archive_month', beta_dict),
      (r'^beta/(?P<year>\d{4})/$',                                                    'archive_year',  beta_dict),
      (r'^beta/$', 'archive_index', beta_dict, "home-beta"),

      )

urlpatterns += patterns (
      '',
      (r'^thedate/$', thedate),
      (r'^(?P<path>.*)/$', static),
      )
