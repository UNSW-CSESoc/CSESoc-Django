from django.db import models

class Invoice(models.Model):
    slug = models.SlugField(max_length=30)
    slug.primary_key = True
    company = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    discount = models.IntegerField()
    hash = models.CharField(max_length=32)
    students_login = models.BooleanField(default=False)
