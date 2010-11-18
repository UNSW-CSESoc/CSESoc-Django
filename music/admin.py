from django.contrib import admin
from csesoc.music.models import *

class SongVoteInline(admin.StackedInline):
   model = SongVote
   extra = 1

class SongAdmin(admin.ModelAdmin):
   list_display = ['title', 'artist', 'submitter', 'submitter_hassong']
   inlines = (SongVoteInline,)
   search_fields =  ["title", "artist", "submitter__username"]

class SongVoteAdmin(admin.ModelAdmin):
   list_display = ['amount', 'song', 'voter']
   search_fields = ["voter__username", "song__title", "song__artist", "amount"]

admin.site.register(Song, SongAdmin)
admin.site.register(SongVote, SongVoteAdmin)

