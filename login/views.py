from django.shortcuts import render, render_to_response
from django.contrib.auth import authenticate, login
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
            print ("Invalid login details: %s, %s" % (username, password))
            return HttpResponse("Invalid login details supplied.")
    else:
        return render_to_response('login/login.html', {}, context)
