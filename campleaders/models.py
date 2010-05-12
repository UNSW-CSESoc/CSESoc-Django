from django.db import models
from csesoc import campglobals

class AwkwardQuestion(models.Model):
   question = models.TextField()
   def __unicode__(self):
      return self.question

class Application(models.Model):
   full_name = models.CharField(max_length=100)
   student_number = models.CharField(max_length=8)
   contact_number = models.CharField(max_length=15)
   cse_username = models.CharField(max_length=15, verbose_name='CSE username')
   gender = models.CharField(max_length=1, choices=campglobals.GENDER_CHOICES)
   accepted = models.BooleanField(default=False)

   shirt_size = models.CharField(max_length=2, choices=campglobals.SHIRT_CHOICES, help_text='Preferred shirt size if chosen to be a leader?')
   cse_program = models.CharField(max_length=2, choices=campglobals.PROGRAM_CHOICES, verbose_name='CSE program')

   payment_status = models.CharField(max_length=1, choices=campglobals.PAYMENT_CHOICES, default='N')
   medical_form = models.BooleanField(default=False)

   year_or_stage = models.IntegerField(verbose_name='Year/Stage')
   year = models.IntegerField(verbose_name='Application Year', editable=False)
   dietary = models.TextField(help_text='Do you have any special dietary requirements', blank=True)
   medical = models.TextField(help_text='Do you have any medical conditions that should be disclosed?', blank=True)
   FIRST_AID_CHOICES = (
         ('Y', 'Yes'),
         ('M', 'Yes, but expired'),
         ('N', 'No, but I can still be a leader!')
         )
   first_aid_qualifications = models.CharField(max_length=1, choices=FIRST_AID_CHOICES, help_text='Do you have any medical/first aid qualifications?')
   q1 = models.TextField(help_text='Why do you want to be a CSE Camp leader?')
   q2 = models.TextField(help_text='What do you think is the purpose of CSE Camp?')
   q3 = models.TextField(help_text='What experience have you had in leadership roles and/or working in groups?')
   q4 = models.TextField(help_text='As a leader, what do you think your responsibilities at CSE Camp will entail?')
   #dodgy hacks to add an remove questions
   q5 = models.TextField(help_text='What personal attributes or characteristics can you bring to CSE Camp?', verbose_name="Old Q5", blank=True)
   q6 = models.TextField(help_text='What would you do if one of the members in your group claims that he/she is being harassed by other people in the group?', verbose_name="Old Q6", blank=True)
   q7 = models.TextField(help_text='What would you do if one member of the group is being excluded or feeling shy in getting involved in group activities?', verbose_name="Old Q7", blank=True)
   q8 = models.TextField(help_text='If a member of your group is underage and wants to drink, what will you advise him/her to do?',verbose_name="Q5")
   q9question = models.ForeignKey(AwkwardQuestion)
   q9 = models.TextField(verbose_name="Q6")

   def __unicode__(self):
      return self.full_name

