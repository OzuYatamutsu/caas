from django.db import models

class Catfact(models.Model):
	_id = models.CharField(max_length=32)
	text = models.CharField(max_length=4096)

class Meta(models.Model):
	_id = models.CharField(max_length=32)
	source = models.CharField(max_length=1024)
	url = models.CharField(max_length=2000)
