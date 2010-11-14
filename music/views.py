# Create your views here.
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from csesoc.music.models import *
from csesoc import settings
from django.template import Library

# presently using generic views for everything. add custom views here as needed

@login_required
def music_submit_song(request):
    songs = Song.objects.all()
    votes = SongVote.objects.filter(voter=request.user)
    votesHash = {}
    finalList = []
    for v in votes:
       votesHash[v.song.id] = v.amount
    for s in songs:
       newS = {}
       newS["song"] = s
       if s.id in votesHash:
          newS["vote"] = votesHash[s.id]
       else:
          newS["vote"] = 0

       newS["states"] = calcVisibility(newS["vote"])
       finalList.append(newS)


    if request.method == "POST":
        # LOL CHECK
        title = request.POST['title']
        artist = request.POST['artist']
        notes = request.POST['notes'] if 'notes' in request.POST else ""
        if 'hassong' in request.POST:
           hassong = "on" == request.POST['hassong']
        else:
           hassong = False

        # submit complete, show a little <thanks> note, and display form again
        songdetails =  (artist + " - " + title)

        s = Song(artist=artist, title=title, notes=notes, submitter_hassong=hassong, submitter=request.user)
        s.save()

        return render_to_response('music.html', {'submitted': True, 'songdetails': songdetails, 'songs': finalList})

    else:
        # yay submit a song template
        return render_to_response('music.html', {'songs': finalList, 'submitted': False})

# returns a list for disabled state for up, none, and down
def calcVisibility(voteAmt):
   res = []
   res.append(True if voteAmt > 0 else False)
   res.append(True if voteAmt == 0 else False)
   res.append(True if voteAmt < 0 else False)
   return res 


@login_required
def music_vote(request):
    if request.method == "POST":
        song_id = request.POST['song_id']
        vote = request.POST['vote']
        voteAmt = 0
        if vote == "up":
            voteAmt = 1
        elif vote == "none":
            voteAmt = 0
        else:
            voteAmt = -1

        # find the song
        s = Song.objects.get(id=song_id)
        u = request.user
        s.vote(u, voteAmt)

        res = str(s.votes())
        for s in calcVisibility(voteAmt):
           res += ";" + str(s)


        return HttpResponse(res)

