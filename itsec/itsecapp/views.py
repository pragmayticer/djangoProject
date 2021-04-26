from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
# Create your views here.
def home_view(request):
    return HttpResponse("ok")
