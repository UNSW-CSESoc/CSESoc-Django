from django.contrib import admin

from csesoc.posts.models import Post
from csesoc.posts.models import Event
from csesoc.posts.models import News

admin.site.register(Post)
admin.site.register(Event)
admin.site.register(News)
