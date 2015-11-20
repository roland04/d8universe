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
                return HttpResponse("Your d8universe account is disabled.")
        else:
            print ("Invalid login details")
            return HttpResponse("Invalid login details supplied.")

    return render_to_response('website/index.html', {}, context)

def user_logout(request):
    context = RequestContext(request)
    logout(request)
    return HttpResponseRedirect('/')
