from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
# Create your views here.
def home_view(request):
    return render(request, "./base.html")
    #return HttpResponse("ok")

def login_view(request):
    #hier dann das lesen der Karte....
    return render(request, "./login.html")
    #return HttpResponse("Ok")

def read_card(request):
    return HttpResponse("ok")