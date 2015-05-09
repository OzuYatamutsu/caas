from django.http import HttpResponse
from django.template import RequestContext, loader
from caas_app.models import Catfact, Meta
from rand import randrange
import mongoengine

user = authenticate(username=username, password=password)
assert isinstance(user, mongoengine.django.auth.User)

def index(request):
	pass
