from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Ingredient(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

class Alias(models.Model):
    realName = models.ForeignKey(Ingredient)

class Thing(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    ingredients = models.ManyToManyField(Ingredient)
    slug = models.SlugField(unique=True)
    user = models.ForeignKey(User, blank=True, null=True)