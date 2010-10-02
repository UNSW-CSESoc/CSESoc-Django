from django.contrib import admin
from csesoc.suggestions.models import *

class SuggestionAdmin(admin.ModelAdmin):
   date_hierarchy = 'last_modified'

class CommentAdmin(admin.ModelAdmin):
   date_hierarchy = 'created'

admin.site.register(Suggestion, SuggestionAdmin)
admin.site.register(Comment, CommentAdmin)
