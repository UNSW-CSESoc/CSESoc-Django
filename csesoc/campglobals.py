PROGRAM_CHOICES = (
      ('CS', 'Computer Science'),
      ('CE', 'Computer Engineering'),
      ('SE', 'Software Engineering'),
      ('BI', 'Bioinformatics'),
      ('FF', 'Flexible First Year Engineering'),
      ('CM', 'Coursework Masters'),
      ('RM', 'Research Masters'),
      ('PD', 'Ph.D'),
      ('OT', 'Other'),
      )

GENDER_CHOICES = (
      ('M', 'Male'),
      ('F', 'Female'),
      )
      

PAYMENT_CHOICES = (
      ('N', 'Not Paid'),
      ('D', 'Deposit Paid'),
      ('A', 'Paid Arc Amount'),
      ('F', 'Paid in Full'),
      )

SHIRT_CHOICES = (
    ('S', 'Mens - Small'),
    ('M', 'Mens - Medium'),
    ('L', 'Mens - Large'),
    ('XL', 'Mens - Extra Large'),
    ('XXL', 'Mens - XXL'),
    ('6', 'Ladies - 6'),
    ('8', 'Ladies - 8'),
    ('10', 'Ladies - 10'),
    ('12', 'Ladies - 12'),
    ('14', 'Ladies - 14'),
    ('16', 'Ladies - 16'),
    )



def make_accepted(modeladmin, request, queryset):
  queryset.update(accepted=True)
make_accepted.short_description = "Accept Leaders"

def mark_depositpaid(modeladmin, request, queryset):
   queryset.update(payment_status='D')
mark_depositpaid.short_description = "Deposit Paid"

def mark_fullpaid(modeladmin, request, queryset):
   queryset.update(payment_status='F')
mark_fullpaid.short_description = "Paid Full"

def mark_arcpaid(modeladmin, request, queryset):
   queryset.update(payment_status='A')
mark_arcpaid.short_description = "Arc Paid"

def mark_medicalyes(modeladmin, request, queryset):
   queryset.update(medical_form=True)
mark_medicalyes.short_description = "Medical Form Handed In"

