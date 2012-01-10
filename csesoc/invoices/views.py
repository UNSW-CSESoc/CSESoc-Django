import uuid
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from django.conf import settings
from csesoc.paypal.standard.forms import PayPalPaymentsForm
from csesoc.invoices.models import *

def invoice_detail(request, slug, hash):
    product = get_object_or_404(Invoice, slug=slug, hash=hash)

    price = product.price - product.discount
    paypal_price = price * 1.025
    paypal = {
            'amount': paypal_price,
            'item_name': product.title,
            'item_number': product.slug,

            # Unique invoice ID
            'invoice': str(uuid.uuid1()),

            'return_url': settings.SITE_DOMAIN + "invoice/" + product.slug + "/" + str(product.hash),
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
        'discount': "-$%.2f"%product.discount,
        'total_price' : "$%.2f"%(price),
        'paypal_price' : "$%.2f"%(paypal_price)
        }, RequestContext(request))
