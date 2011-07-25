from django.db import models
from django.template.loader import render_to_string
from datetime import date
from django.template import RequestContext
from csesoc import settings
from django.core.files.storage import FileSystemStorage

class Sponsor(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    website = models.URLField(verify_exists=False)
    logo = models.ImageField(upload_to='sponsors')
    alt_text = models.CharField(max_length=150)
    amount_paid = models.PositiveIntegerField()
    start_date = models.DateField(auto_now_add=True, editable=False)
    expiry_date = models.DateField()
    html_override = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.name

    def get_linked_logo(self):
        return render_to_string("sponsor-linked-logo.html", { 'object': self, 'SPONSOR_LOGOS_URL' : settings.MEDIA_URL + 'sponsors/' }) 

    def get_rendered_html(self):
        return render_to_string("sponsor-description.html", { 'object': self, 'SPONSOR_LOGOS_URL' : settings.MEDIA_URL + 'sponsors/' })

    def is_default_html(self):
        return self.html_override is None or self.html_override == ""
