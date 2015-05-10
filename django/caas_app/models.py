from mongoengine import *

class Catfact(Document):
    _id = StringField(max_length=32)
    text = StringField(max_length=4096)

    def __unicode__(self):
        return self.text

class Meta(Document):
    _id = StringField(max_length=32)
    source = StringField(max_length=1024)
    url = StringField(max_length=2000)

    def __unicode__(self):
        return "Source: " + self.source + ", URL: " + self.url

class Intro(Document):
    _id = StringField(max_length=32)
    text = StringField(max_length=4096)

    def __unicode__(self):
        return self.text

class Newsub(Document):
    _id = StringField(max_length=32)
    text = StringField(max_length=4096)

    def __unicode__(self):
        return self.text

class Unsub(Document):
    _id = StringField(max_length=32)
    text = StringField(max_length=4096)

    def __unicode__(self):
        return self.text

class Notrecog(Document):
    _id = StringField(max_length=32)
    text = StringField(max_length=4096)

    def __unicode__(self):
        return self.text
