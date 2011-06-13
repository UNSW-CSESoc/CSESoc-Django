from csesoc.scheduler.models import Availability
from django import template
register = template.Library()
@register.filter
def showlevel(value):
   return Availability.get_level_display(value)

