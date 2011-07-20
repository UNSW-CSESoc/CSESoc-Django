from polls.models import Poll
from polls.models import PollOption
from django.contrib import admin

class PollOptionInline(admin.TabularInline):
    model = PollOption
    extra = 2

class PollAdmin(admin.ModelAdmin):
    inlines = [PollOptionInline]

    list_display = ('question', 'pubDate', 'endDate')

admin.site.register(Poll, PollAdmin)
