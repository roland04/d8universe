from django.shortcuts import render, render_to_response
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext

def user_login(request):
    context = RequestContext(request)

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                alert = "%s account is disabled." % request.POST['username']
                return render_to_response('website/alert.html', {"message":alert}, context)
        else:
            alert = "Invalid User or Password."
            return render_to_response('website/alert.html', {"message":alert}, context)

    return render_to_response('website/index.html', {}, context)

def user_logout(request):
    context = RequestContext(request)
    logout(request)
    return HttpResponseRedirect('/')
