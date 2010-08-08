from django.contrib import admin
from csesoc.game.models import Static

class StaticAdmin(admin.ModelAdmin):
   list_display = ('title', 'creation_date', 'slug',)
   def save_model(self, request, obj, form, change):
      obj.save()

admin.site.register(Static, StaticAdmin)

