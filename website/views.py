from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext

def index(request):
    context = RequestContext(request)
    return render_to_response('website/index.html', {}, context)
