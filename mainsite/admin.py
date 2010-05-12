from django.contrib import admin
from csesoc.mainsite.models import Beta,NewsItem,Event,Static

class NewsItemAdmin(admin.ModelAdmin):
   exclude = ('author',)
   def save_model(self, request, obj, form, change):
      if not change:
         obj.author = request.user
      obj.save()

admin.site.register(NewsItem, NewsItemAdmin)

class BetaAdmin(admin.ModelAdmin):
   exclude = ('author',)
   def save_model(self, request, obj, form, change):
      if not change:
         obj.author = request.user
      obj.save()

admin.site.register(Beta, BetaAdmin)

class EventAdmin(admin.ModelAdmin):
   exclude = ('author',)
   def save_model(self, request, obj, form, change):
      if not change:
         obj.author = request.user
      obj.save()

admin.site.register(Event, EventAdmin)

class StaticAdmin(admin.ModelAdmin):
   exclude = ('creator', 'updater',)
   list_filter = ('creator',)
   list_display = ('title', 'creation_date', 'creator', 'slug',)
   def save_model(self, request, obj, form, change):
      if not change:
         obj.creator = request.user
      obj.updater = request.user
      obj.save()

admin.site.register(Static, StaticAdmin)

