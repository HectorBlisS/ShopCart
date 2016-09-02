from __future__ import unicode_literals

from django.db import models

class Product(models.Model):
	nombre = models.CharField(max_length=140)
	price = models.FloatField()
	
