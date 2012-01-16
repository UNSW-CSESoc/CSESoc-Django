from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_save
from django.db.models.signals import pre_delete
from django.contrib.auth.models import User
from django.contrib.contenttypes import generic
from django.template.loader import render_to_string
from django.conf import settings
from datetime import datetime
from tinymce import models as tinymce_models
import os

class Static(models.Model):
   title = models.CharField(max_length=200)
   text = models.HTMLField()
   # HTML mode is broken for tinymce
   #text = tinymce_models.HTMLField()
   template = models.FilePathField(path=os.path.join(settings.PROJECT_PATH, "templates"), match="static.*\.html")
   creation_date = models.DateTimeField(auto_now_add=True)
   creator = models.ForeignKey(User, related_name='page_creator')
   update_date = models.DateTimeField(auto_now=True)
   updater = models.ForeignKey(User, related_name='page_updater')
   slug = models.SlugField(help_text="slug will be used in url generation, keep it simple, stupid.")
   def __unicode__(self):
      return self.title
   def save(self, *args, **kwargs):
      #the db should not contain absolute paths
      #so the database gets fixed on saves
      import re
      self.template = re.sub(r'.*/templates/','',self.template)
      super(Static, self).save(*args, **kwargs) # Call the "real" save() method.

class NewsItem(models.Model):
   headline = models.CharField(max_length=200)
   text = tinymce_models.HTMLField()
   pub_date = models.DateTimeField(default=datetime.now, help_text="News item will appear on homepage starting from date and time specified.")
   author = models.ForeignKey(User)
   def __unicode__(self):
      return self.headline

class Event(models.Model):
   name = models.CharField(max_length=200)
   time = models.DateTimeField()
   location = models.CharField(max_length=200)
   registration_required = models.BooleanField()
   registration_email = models.EmailField(blank=True, help_text="Address to email in order to register")
   volunteers_required = models.BooleanField()
   volunteers_email = models.EmailField(blank=True, help_text="Address to email in order to volunteer")  
   description = tinymce_models.HTMLField(help_text="Description of the event, will appear on the front page.")
   pub_date = models.DateTimeField(default=datetime.now, help_text="Event will appear on homepage starting from date and time specified.")
   author = models.ForeignKey(User)
   def __unicode__(self):
      return self.name

class Beta(models.Model):
   title = models.CharField(max_length=200, default="Beta 09S1 Week X Now Available")
   blurb = models.TextField()
   pdf_url = models.URLField(verify_exists=True, help_text="Link to PDF of this issue of Beta", max_length=500)
   pub_date = models.DateTimeField(default=datetime.now, help_text="Beta will appear on homepage starting from date and time specified.")

   author = models.ForeignKey(User)
   def __unicode__(self):
      return self.title

class StreamItem(models.Model):
   content_type = models.ForeignKey(ContentType)
   object_id = models.PositiveIntegerField()
   pub_date = models.DateTimeField()

   content_object = generic.GenericForeignKey('content_type', 'object_id')

   def get_rendered_html(self):
      template_name = 'stream_item_%s.html' %(self.content_type.name)
      template_name = template_name.replace(' ','_')
      return render_to_string(template_name, { 'object': self.content_object })

# Hook for creating StreamItems

def create_stream_item(sender, instance, signal, *args, **kwargs):
   # Get the instance's content type
   ctype = ContentType.objects.get_for_model(instance)

   # Get the instance's pub date
   #if ctype.name == 'beta':
   #   pub_date = instance.announce_date
   #elif ctype.name == 'somethin else':
   #   pub_date = instance.some_field
   #else:
   #   pub_date = instance.pub_date
   pub_date = instance.pub_date

   # Update or create the corresponding StreamItem
   try:
      si = StreamItem.objects.get(content_type=ctype, object_id=instance.id)
      si.pub_date = pub_date
      si.save()
   except StreamItem.DoesNotExist:
      si = StreamItem(content_type=ctype, object_id=instance.id, pub_date=pub_date)
      si.save()

# Hook for removing StreamItems
def remove_stream_item(sender, instance, signal, *args, **kwargs):
   # Get the instance's content type
   ctype = ContentType.objects.get_for_model(instance)

   # Get the stream item corresponding to the instance being removed, and delete it.
   si = StreamItem.objects.get(content_type=ctype, object_id=instance.id)
   si.delete()

# send a signal on post_save and pre_delete for each of these models
for modelname in [NewsItem, Event, Beta]:
   post_save.connect(create_stream_item, sender=modelname)
   pre_delete.connect(remove_stream_item, sender=modelname)

