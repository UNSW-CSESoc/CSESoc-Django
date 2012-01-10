from django.contrib import admin
from csesoc.invoices.models import *
from django.conf import settings
import md5

class InvoiceAdmin(admin.ModelAdmin):
    def total_price(obj):
        return "$%s"%(str(obj.price - obj.discount))
    def invoice_description(obj):
        return obj.title
    def invoice_number(obj):
        return obj.slug
    def link(obj):
        url = "%sinvoice/%s/%s" % (settings.SITE_DOMAIN, obj.slug, obj.hash)
        return "<a href='%s'>%s</a>"%(url, url)
    link.allow_tags = True

    def hash_function(self, obj):
        return md5.new(str(obj.slug) + str(obj.company)).hexdigest()

    def save_model(self, request, obj, form, change):
        obj.hash = self.hash_function(obj)
        obj.save()

    exclude = ('hash',)
    list_filter = ('company',)
    list_display = (invoice_number,'company',invoice_description,total_price,link)
    search_fields = ['company', '^slug', 'title', '^hash']


admin.site.register(Invoice, InvoiceAdmin)
