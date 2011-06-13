import set_path
set_path.update_path()

from django.core.management import setup_environ
import settings

setup_environ(settings)

from csesoc.murder.models import *

for password in open('murder/passwords.txt'):
   p = Password(text=password[:-1])
   p.save()

for quip in open('murder/quips.txt'):
   q = Quip(text=quip[:-1])
   q.save()


