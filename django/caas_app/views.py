from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from mongoengine import queryset
from caas_app.models import Catfact, Meta, Intro, Newsub, Unsub, Notrecog
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
    response_json = {}
    
    # Unless id specified, get random fact
    if ("id" not in request.GET):        
        if ("include" in request.GET):
            include_params = [x.replace("+", " ").replace("%20", " ") for x in request.GET['include'].split(',')] 
            filter_results = Meta.objects(source__in=include_params) 
            if (filter_results.count() == 0):
                return HttpResponse("No results from source " + str(include_params) + "!")
            id = str(filter_results[randrange(0, filter_results.count())].id)
        elif ("exclude" in request.GET):
            exclude_params = [x.replace("+", " ").replace("%20", " ") for x in request.GET['exclude'].split(',')]
            filter_results = Meta.objects(source__nin=exclude_params)
            if (filter_results.count() == 0):
                return HttpResponse("No results from sources other than " + str(include_params) + "!")

            id = str(filter_results[randrange(0, filter_results.count())].id)
        else:
            # No filters
            id = str(Meta.objects[randrange(0, Meta.objects.count())].id)
    else:
        id = request.GET['id']
        try:
            # Check if ID exists
            Meta.objects().get(_id=request.GET['id'])
        except queryset.DoesNotExist: 
            return HttpResponse("Cat-fact ID " + id + " was not found.")
    
    # Lookup cat-fact ID in database
    cat_fact = Catfact.objects().get(_id=id)
    meta = Meta.objects().get(_id=id)        
    
    # Now parse other arguments here
    if ("intro" in request.GET):
        if (request.GET['intro'] == "yes"):
            cat_fact.text = Intro.objects[randrange(0, Intro.objects.count())].text + " " + cat_fact.text
    if ("newsub" in request.GET):
        if (request.GET['newsub'] == "yes"):
            cat_fact.text = Newsub.objects[randrange(0, Newsub.objects.count())].text + " " + cat_fact.text
    if ("unsub" in request.GET):
        if (request.GET['unsub'] == "yes"):
            cat_fact.text = cat_fact.text + " " + Unsub.objects[randrange(0, Unsub.objects.count())].text
    if ("notrecog" in request.GET):
        if (request.GET['notrecog'] == "yes"):
            cat_fact.text = Notrecog.objects[randrange(0, Notrecog.objects.count())].text + " " + cat_fact.text

    # Now construct JSON response here
    response_json['_id'] = id
    response_json['text'] = cat_fact.text
    response_json['source'] = meta.source
    response_json['url'] = meta.url
    
    return JsonResponse(response_json)
