from django.db import models

class Catfact(models.Model):
    _id = models.CharField(max_length=32)
    text = models.CharField(max_length=4096)

    def __unicode__(self):
        return self.text

class Meta(models.Model):
    _id = models.CharField(max_length=32)
    source = models.CharField(max_length=1024)
    url = models.CharField(max_length=2000)

    def __unicode__(self):
        return "Source: " + self.source + ", URL: " + self.url
