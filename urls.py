from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from csesoc import mainsite
from csesoc import campleaders
from csesoc import settings
from csesoc.game.views import game_static, game_scores, game_static_latest
from csesoc.campleaders.views import apply
from csesoc.campattendees.views import signup
from csesoc.suggestions.views import suggest
from csesoc.sponsors.views import sponsors
from csesoc.mainsite.views import static
from csesoc.mainsite.views import thedate
from csesoc.scheduler.views import join, results
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
      # admin site
      #(r'^admin/(.*)', admin.site.root),
      (r'^admin/(.*)', 'csesoc.auth.backends.admin_wrapper'),
      # Statics path
      (r'static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_URL}),
      # login redirect
      (r'accounts/login/$', 'csesoc.auth.backends.cse_login',),
      # (r'accounts/login/$', 'django.contrib.auth.views.login'),
      # camp leader applications
      (r'^apply/$', apply),
      # camp attendee applications
      (r'^signup/$', signup),
      # suggestions form
      (r'^suggestions/$', suggest),
      # scheduler signup
      (r'^oweek/signup/$', join),
      (r'^oweek/slots/$', results),
      # sponsors page
      (r'^sponsors/$', sponsors),

      # urls for murder
      (r'^murder/', include('csesoc.murder.urls')),

      # url for the game
      (r'^game/scores/(?P<year>[0-9]*)$', game_scores),
      (r'^game/$', game_static_latest),
      (r'^game/(?P<path>.*)$', game_static),
)
urlpatterns += patterns(
      'django.views.generic.date_based',
      # all news sources
      (r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/$',               'archive_day',   tumblog_dict),
      (r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/$',                                'archive_month', tumblog_dict),
      (r'^(?P<year>\d{4})/$',                                                    'archive_year',  tumblog_dict),
      (r'^$', 'archive_index', tumblog_dict, "home"),

      # news
      (r'^news/(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/$',               'archive_day',   news_dict),
      (r'^news/(?P<year>\d{4})/(?P<month>[a-z]{3})/$',                                'archive_month', news_dict),
      (r'^news/(?P<year>\d{4})/$',                                                    'archive_year',  news_dict),
      (r'^news/$', 'archive_index', news_dict, "home-news"),

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

