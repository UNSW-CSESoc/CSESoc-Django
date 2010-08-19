from django.contrib import admin
from csesoc.game.models import *

class PuzzleAdmin(admin.ModelAdmin):
   list_display = ('title', 'next_puzzle', 'points', 'creation_date', 'slug')
   def save_model(self, request, obj, form, change):
      obj.save()

class PlayerProgressInline(admin.StackedInline):
   model = PlayerProgress
   extra = 2

class PlayerAdmin(admin.ModelAdmin):
   list_display = ['username', 'score', 'upto', 'rank']
   search_fields = ['username']
   inlines = (PlayerProgressInline,)
   model = Player

class GameAdmin(admin.ModelAdmin):
   model = Game

class AttemptAdmin(admin.ModelAdmin):
   list_display = ['attempt_time', '__unicode__']
   search_fields = ['progress__player__username', 'progress__puzzle__title', 'progress__puzzle__slug', 'attempt']
   model = PlayerAttempt

admin.site.register(Puzzle, PuzzleAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(Player, PlayerAdmin)
admin.site.register(PlayerAttempt, AttemptAdmin)

