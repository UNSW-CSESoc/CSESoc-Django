from datetime import datetime

from django.conf.urls.defaults import *
from django.contrib import admin

from csesoc import mainsite
from csesoc import settings
from csesoc.campattendees.views import signup
from csesoc.campleaders.views import apply
from csesoc.game.views import game_scores, game_static, game_static_latest
from csesoc.mainsite.views import static, thedate, calendar
from csesoc.scheduler.views import join, results
from csesoc.sponsors.views import sponsors
from csesoc.suggestions.views import suggest

admin.autodiscover()

urlpatterns = patterns(
    '',

    # Admin site
    (r'^admin/(.*)', 'csesoc.auth.backends.admin_wrapper'),

    # Statics path
    (r'static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_URL}),

    # Login redirect
    (r'accounts/login/$', 'csesoc.auth.backends.cse_login'),

     # Sponsors
    (r'^sponsors/$', sponsors),

    # Camp leader applications
    (r'^apply/$', apply),
    # Camp attendee applications
    (r'^signup/$', signup),

#    # Suggestions form
#    (r'^suggestions/', include('csesoc.suggestions.urls')),

    # O-Week signup
    (r'^oweek/signup/$', join),
    (r'^oweek/slots/$', results),

    # Murder
    (r'^murder/', include('csesoc.murder.urls')),

    # News-related stuff
    (r'^', include('csesoc.mainsite.urls')),

    # The date
    (r'^thedate/$', thedate),

    # Full calendar page
    (r'^home/calendar/$', calendar),

    # Miscellaneous articles
    (r'^(?P<path>.*)/$', static),

    # The Game URLs
    #(r'^game/scores/(?P<year>[0-9]*)$', game_scores),
    #(r'^game/scores$', game_scores, {'year':''}),
    #(r'^game/$', game_static_latest),
    #(r'^game/(?P<path>.*)$', game_static),

    # Music/Playlist URLs 
    #(r'^music/$', music_submit_song),
    #(r'^music/vote/$', music_vote),
)

