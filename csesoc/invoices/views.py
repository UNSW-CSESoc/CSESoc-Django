import uuid
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from django.conf import settings
from csesoc.paypal.standard.forms import PayPalPaymentsForm
from csesoc.invoices.models import *

def invoice_thanks(request, slug):
    product = get_object_or_404(Invoice, slug=slug)
    return render_to_response('product_thanks.html', {
        'product':product,
	'title':"Thanks!",
        }, RequestContext(request))

def invoice_detail(request, slug, hash):
    product = get_object_or_404(Invoice, slug=slug, hash=hash)

    # The direct debit price with discount applied
    price = product.price - product.discount

    # The paypal price is the direct debit price plus a 2.5% fee
    paypal_price = price * 1.025

    # See the following guide for more details on variables
    # https://cms.paypal.com/cms_content/US/en_US/files/developer/PP_WebsitePaymentsStandard_IntegrationGuide.pdf
    paypal = {
            'amount': paypal_price,
            'currency_code' : "AUD",
            'no_shipping' : 1, # Don't prompt for an address
            'no_note' : 1, # Don't prompt for a note

            'item_name': '%s: %s'%(str(product.slug),product.title),
            # Need a 150x150px image
            #'image_url' : settings.SITE_DOMAIN + '/static/header/header.png',

            # Unique invoice ID
            'invoice': str(uuid.uuid1()),

            # The URL they will return to
            'return_url': settings.SITE_DOMAIN + "invoice/thanks/" + product.slug,

            # The URL they will cancel to
            'cancel_return': settings.SITE_DOMAIN + "invoice/" + product.slug + "/" + str(product.hash),
            }

    form = PayPalPaymentsForm(initial=paypal)
    if settings.DEBUG:
        rendered_form = form.sandbox()
    else:
        rendered_form = form.render()
    return render_to_response('product_detail.html', {
        'product':product,
        'form': rendered_form,
        'price' : "$%.2f"%product.price,
        'discount': "($%.2f)"%product.discount,
        'total_price' : "$%.2f"%(price),
        'paypal_price' : "$%.2f"%(paypal_price),
	'title' : "Invoice #%s"%str(product.slug)
        }, RequestContext(request))
