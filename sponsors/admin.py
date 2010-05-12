from django.contrib import admin
from csesoc.sponsors.models import Sponsor

class SponsorAdmin(admin.ModelAdmin):
  list_display = ('name', 'website', 'expiry_date',)

admin.site.register(Sponsor, SponsorAdmin)
