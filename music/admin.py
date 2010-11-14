from django.contrib import admin
from csesoc.music.models import *


class SongAdmin(admin.ModelAdmin):
   pass

admin.site.register(Song, SongAdmin)
admin.site.register(SongVote)

