from django.shortcuts import render_to_response, get_list_or_404
from django.template import RequestContext
from csesoc.sponsors.models import Sponsor
from datetime import date
from django.conf import settings

def sponsors(request):
    return render_to_response('sponsor.html', 
                              {'allSponsors' : Sponsor.objects.order_by('amount_paid').reverse().filter(expiry_date__gte=date.today),
                               'nav' : 'oursponsors',}, 
                              context_instance = RequestContext(request))

def sponsorsList(request):
    return list(Sponsor.objects.order_by('amount_paid').reverse().filter(expiry_date__gte=date.today))
    


