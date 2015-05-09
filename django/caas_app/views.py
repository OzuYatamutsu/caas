from django.shortcuts import render
from caas_app.models import Catfact, Meta
from random import randrange

def index(request):
    # Select random fact
    rand_id = str(Meta.objects[randrange(0, Meta.objects.count())].id)
    
    # Pull data from db
    cat_fact = Catfact.objects().get(_id=rand_id)
    meta = Meta.objects().get(_id=rand_id)

    # Push to template
    context = {'cat_fact': cat_fact, 'meta': meta}

    return render(request, "index.html", context)
