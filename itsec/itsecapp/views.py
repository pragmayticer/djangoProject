from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from django.contrib.auth.decorators import login_required

@login_required
def home_view(request):
    print(request.user.email)
    return render(request, "./base.html")
    #return HttpResponse("ok")