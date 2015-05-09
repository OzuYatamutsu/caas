from django.shortcuts import render
from django.http import HttpResponse
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

    return render(request, 'index.html', context)

def api(request):
    id = ""
    cat_fact = None
    meta = None
    response_str = ""
    
    # Unless id specified, get random fact
    if (id not in request.GET):
        id = str(Meta.objects[randrange(0, Meta.objects.count())].id)
    else:
        id = request.GET['id']
        try:
            # Check if ID exists
            Meta.objects().get(_id=request.GET['id'])
        except Exception: # TODO: specific type
            return HttpResponse("Cat-fact ID " + id + " was not found.")
    
    # Lookup cat-fact ID in database
    cat_fact = Catfact.objects().get(_id=rand_id)
    meta = Meta.objects().get(_id=rand_id)        
    
    # Now parse other arguments here
    # TODO: args

    # Now construct JSON response here
    # TODO: response from str

    return HttpResponse(response_str)
