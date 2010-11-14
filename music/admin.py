from django.contrib import admin
from csesoc.music.models import *

class SongVoteInline(admin.StackedInline):
   model = SongVote
   extra = 1

class SongAdmin(admin.ModelAdmin):
   list_display = ['title', 'artist', 'submitter', 'submitter_hassong']
   inlines = (SongVoteInline,)

class SongVoteAdmin(admin.ModelAdmin):
   list_display = ['amount', 'song', 'voter']

admin.site.register(Song, SongAdmin)
admin.site.register(SongVote, SongVoteAdmin)

