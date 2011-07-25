from csesoc import settings

def sponsors_list(request):
  from csesoc.sponsors.models import Sponsor
  sponsors = Sponsor.objects.order_by('-amount_paid', 'name')
  return { 'sponsors' : sponsors }

def media_url(request):
  return { 'MEDIA_URL' : settings.MEDIA_URL }

def static_url(request):
  return { 'STATIC_URL' : settings.STATIC_URL }
