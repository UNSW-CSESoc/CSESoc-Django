import uuid
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from django.conf import settings
from csesoc.paypal.standard.forms import PayPalPaymentsForm
from csesoc.invoices.models import *

def invoice_detail(request, slug):
    product = get_object_or_404(Invoice, slug=slug)

    paypal = {
            'amount': product.price - product.discount,
            'item_name': product.title,
            'item_number': product.slug,

            # Unique invoice ID
            'invoice': str(uuid.uuid1()),

            'return_url': settings.SITE_DOMAIN + "invoice/" + product.slug,
            'cancel_return': settings.SITE_DOMAIN + "invoice/" + product.slug,
            }

    form = PayPalPaymentsForm(initial=paypal)
    if settings.DEBUG:
        rendered_form = form.sandbox()
    else:
        rendered_form = form.render()
    return render_to_response('product_detail.html', {
        'product':product,
        'form': rendered_form,
        }, RequestContext(request))
