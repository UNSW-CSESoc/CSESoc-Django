from django.contrib import admin
from csesoc.scheduler.models import Slot, Availability

admin.site.register(Slot)
admin.site.register(Availability)

