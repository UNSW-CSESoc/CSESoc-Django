from django.conf import settings

def sponsors_list(request):
  from csesoc.sponsors.models import Sponsor
  sponsors = Sponsor.objects.order_by('-amount_paid', 'name')
  return { 'sponsors' : sponsors }
