from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class Tag(models.Model):
	name = models.CharField(max_length=20)

class Recipe(models.Model):
	title = models.CharField(max_length=20)
	text = models.TextField()
	tags = models.ManyToManyField(Tag)

class MyUser(AbstractUser):
	nickname = models.CharField(max_length=10)
	recipe = models.ManyToManyField(Recipe)

