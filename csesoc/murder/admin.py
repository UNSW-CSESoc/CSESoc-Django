from django.contrib import admin
from django import forms
from csesoc.murder.models import *
from django.db.models import Q

class GamePlayerInline(admin.StackedInline):
   model = GamePlayer
   extra = 5

class GameAdmin(admin.ModelAdmin):
   inlines = (GamePlayerInline,)
   exclude = ('slug',)

class KillAdmin(admin.ModelAdmin):
   fields = ('round','killer')

# custom validation to stop 2 rounds occuring at once

# ASCII art to describe the 4 different clash cases:
# stars are the round being created, dashed rounds clash (a,b,c,d)
#       ********************
#     --a--    --b--     --c--
#   -------------d--------------

class MyRoundAdminForm(forms.ModelForm):
   class Meta:
      model = Round
   def clean(self): # called after standard field validation
      cleaned_data = self.cleaned_data
      start = cleaned_data.get("start")
      end = cleaned_data.get("end")
      if cmp(start,end) >= 0:
         raise forms.ValidationError("A round must end after it beings")
      q = Q(start__lte=start, end__gte=start) | Q(start__gte=start, end__lte=end) | Q(start__lte=end, end__gte=end) | Q(start__lte=start, end__gte=end)
      clashes = Round.objects.filter(q)
      if clashes:
         raise forms.ValidationError("Clash with existing round(s): " + unicode(clashes))
      return cleaned_data

class RoundAdmin(admin.ModelAdmin):
   form = MyRoundAdminForm

admin.site.register(Player)
admin.site.register(Password)
admin.site.register(Quip)
admin.site.register(Game, GameAdmin)
admin.site.register(Round, RoundAdmin)
#admin.site.register(GamePlayer)
admin.site.register(RoundPlayer)
admin.site.register(Kill, KillAdmin)

