from django.contrib import admin
from csesoc.invoices.models import *
from django.conf import settings
from django import forms
import md5, re

class InvoiceAdminForm(forms.ModelForm):
    class Meta:
        model = Invoice

    def clean_slug(self):
        slug = self.cleaned_data.get('slug')
        if not re.match(r'^[0-9]{8}$', slug):
            raise forms.ValidationError("Must be made of 8 digits!")
        else:
            return slug

class InvoiceAdmin(admin.ModelAdmin):
    form = InvoiceAdminForm

    def price(obj):
        return "$%s"%(str(obj.price))
    def discount(obj):
        return "($%s)"%(str(obj.discount))
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
    list_display = (invoice_number,'company',invoice_description,price,discount,link)
    search_fields = ['company', '^slug', 'title', '^hash']


admin.site.register(Invoice, InvoiceAdmin)
