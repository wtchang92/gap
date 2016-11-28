from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Task(models.Model):
	title = models.CharField(max_length=80, null=False, blank= False)
	description = models.TextField(max_length=150, null=False, blank= False)
	added = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __string__(self):
		return self.title