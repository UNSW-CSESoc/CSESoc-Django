from django.db import models

class Invoice(models.Model):
    slug = models.SlugField(max_length=30)
    company = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    discount = models.IntegerField()
