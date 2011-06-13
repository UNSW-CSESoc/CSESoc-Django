from django.conf.urls.defaults import *
from django.conf import settings
from csesoc.suggestions.views import *

urlpatterns = patterns('',
   # URLs for suggestions applcation
   (r'^$', list_suggestions),
   (r'^(?P<suggestion>[0-9]+)/$', comments),
   (r'^new/$', suggest),
)

