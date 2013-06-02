from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import RequestContext

from .services import (auth, rain_service, flood_service, schools_service)

#APP_ID = "22c8b97c40300511021ca57438088b44"
#APP_SECRET = "a4wk8-edlm6-7213k"

APP_ID = "609a3eca35048e61d70edaf5f7479895"
APP_SECRET = "13u3k-g2wk9-vj9k5"

def home(request):
    return render_to_response('index.html', {},
                              context_instance=RequestContext(request))

def rain_info(request):
    (token, token_expires) = auth(APP_ID, APP_SECRET)
    result = rain_service(token)
    return HttpResponse(result, mimetype='application/json')

def flood_info(request):
    (token, token_expires) = auth(APP_ID, APP_SECRET)
    result = flood_service(token)
    return HttpResponse(result, mimetype='application/json')

def schools_info(request):
    (token, token_expires) = auth(APP_ID, APP_SECRET)
    result = schools_service(token)
    return HttpResponse(result, mimetype='application/json')
