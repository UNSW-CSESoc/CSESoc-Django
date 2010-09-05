from django.db import models
from django.template.loader import render_to_string
from datetime import datetime
from django.template import RequestContext
from csesoc import settings
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.db.models.signals import post_save
from django.db.models.signals import pre_delete

class News(models.Model):
    headline = models.CharField(max_length = 200)
    text = models.TextField()
    pub_date = models.DateTimeField(default = datetime.now, help_text = "News item will only appear on site after this date.")
    author = models.ForeignKey(User)
    def __unicode__(self):
        return self.headline
 
class Event(models.Model):
    name = models.CharField(max_length = 200)
    time = models.DateTimeField()
    location = models.CharField(max_length = 200)
    registration_required = models.BooleanField()
    registration_email = models.EmailField(blank = True, help_text = "Address to email in order to register.")
    volunteers_required = models.BooleanField()
    volunteers_email = models.EmailField(blank = True, help_text = "Address to email in order to volunteer.")
    description = models.TextField()
    pub_date = models.DateTimeField(default = datetime.now, help_text = "Event will only appear on site after this date.")
    author = models.ForeignKey(User)
    def __unicode__(self):
        return self.name

#A general class to store all posts, both News and Events
class Post(models.Model):
    post_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    pub_date = models.DateTimeField()

    #The News or Event object associated with this Post
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    def get_rendered_html(self):
        return "hello"
        #self.content_object.get_rendered_html()
#        template_name = 'stream_item_%s.html' %(self.content_type.name)
#        template_name = template_name.replace(' ','_')
#        return render_to_string(template_name, { 'object': self.content_object })

def create_post(sender, instance, signal, *args, **kwargs):
    instance_type = ContentType.objects.get_for_model(instance)
    instance_id = instance.id
    pub_date = instance.pub_date

    #Update or create a post for the news or event
    post, created = Post.objects.get_or_create(post_type = instance_type, object_id = instance_id, pub_date = pub_date)
    if not created:
        post.pub_date = pub_date;
    post.save() 

def remove_post(sender, instance, signal, *args, **kwargs):
    instance_type = ContentType.objects.get_for_model(instance)
    instance_id = instance.id

    #Get the post corresponding to the news or event being removed and delete it as well
    si = Post.objects.get(content_type = instance_type, object_id = instance_id)
    si.delete()

#Send a signal on post_save and pre_delete for each of these models
for modelname in [News, Event]:
    post_save.connect(create_post, sender=modelname)
    pre_delete.connect(remove_post, sender=modelname)

