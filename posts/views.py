from django.shortcuts import render_to_response
from django.template import RequestContext
from csesoc.posts.models import Post
from csesoc.sponsors.views import sponsorsList
from csesoc import settings

def recentPosts(request, offset = '0'):
    recentPosts = Post.objects.order_by('pub_date')[10 * int(offset):10 * int(offset) + 10]
    return render_to_response('posts.html',
                              {'posts' : recentPosts, 
                               'nextOffset' : str(int(offset) + 1),
                               'prevOffset' : str(max([int(offset) - 1, 0])),
                               'allSponsors' : sponsorsList(request)}, 
                              context_instance = RequestContext(request))
