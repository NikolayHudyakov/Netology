from django.db import models


class Phone(models.Model):
    name = models.CharField()
    price = models.IntegerField()
    image = models.CharField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField()


