from django.contrib import admin
from csesoc.game.models import *

class PuzzleAdmin(admin.ModelAdmin):
   list_display = ('title', 'creation_date', 'slug',)
   def save_model(self, request, obj, form, change):
      obj.save()

class PlayerProgressInline(admin.StackedInline):
   model = PlayerProgress
   extra = 2

class PlayerAdmin(admin.ModelAdmin):
   inlines = (PlayerProgressInline,)
   model = Player

class GameAdmin(admin.ModelAdmin):
   model = Game

class AttemptAdmin(admin.ModelAdmin):
   model = PlayerAttempt

admin.site.register(Puzzle, PuzzleAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(Player, PlayerAdmin)
admin.site.register(PlayerAttempt, AttemptAdmin)

