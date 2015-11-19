from django.shortcuts import render, render_to_response
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from login.forms import LoginForm

def user_login(request):
    context = RequestContext(request)

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    return HttpResponse("Your d8universe account is disabled.")
            else:
                print ("Invalid login details")
                return HttpResponse("Invalid login details supplied.")
    else:
        form = LoginForm()

    return render_to_response('login/index.html', {'form':form}, context)

def user_logout(request):
    context = RequestContext(request)
    logout(request)
    return HttpResponseRedirect('/')
