from django.conf import settings
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import RequestContext

from .services import (auth, rain_service, flood_service, schools_service)

APP_ID = settings.APP_ID
APP_SECRET = settings.APP_SECRET

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
