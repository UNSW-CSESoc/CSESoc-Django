from django.conf.urls.defaults import *
from django.conf import settings
from csesoc.murder.views import *

# Uncomment the next two lines to enable the admin:

urlpatterns = patterns('',
      # URLs for murder applcation
      (r'^$', gamelist),
      (r'^(?P<game>[^/]*)/$', index),
      (r'^(?P<game>[^/]*)/scoreboard/$', scoreboard),
      (r'^(?P<game>[^/]*)/kills/$', newkills),
      (r'^(?P<game>[^/]*)/kills/(?P<roundid>\d+)/$', roundkills),
      (r'^(?P<game>[^/]*)/myvictim/$', myvictim),
)

