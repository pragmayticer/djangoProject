from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User,AnonymousUser
from .models import RFID_Daten

from django.contrib.auth.decorators import login_required
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import MySQLdb
from datetime import datetime
import time

def home_view(request):
    reader = SimpleMFRC522()
    rfid_id: int = 0
    rfid_id, text = reader.read()
    if request.user.is_anonymous:
        return render(request, "./base.html")
    current_usermail = request.user.email
    current_user = User.objects.get(email=current_usermail)
    all_RFID_Daten: QuerySet=RFID_Daten.objects.filter(user=current_user)
    print(all_RFID_Daten)
    if current_user.is_superuser:
        current_RFID = int(all_RFID_Daten[0].RFID_Id)
        if current_RFID == rfid_id:
            all_RFID_Daten: QuerySet=RFID_Daten.objects.all()
            b = RFID_Daten(RFID_Id=current_RFID, name=current_user.username, login=datetime.now(), user=current_user)
            b.save()
            return render(request, "./base.html", {'posts': all_RFID_Daten})
    else:
        current_RFID = int(all_RFID_Daten[0].RFID_Id)
        print(current_RFID)
        print(rfid_id)
        if rfid_id == current_RFID:
            b = RFID_Daten(RFID_Id=current_RFID, name=current_user.username, login=datetime.now(), user=current_user)
            b.save()
            return render(request, "./base.html", {'posts': all_RFID_Daten})
        else:
            print("nicht gleich")
    return HttpResponse("Kein Zugriff möglich")

def login_view(request):
    return redirect("https://localhost:8000/admin/login/")

def logout_view(request):
    return redirect("https://localhost:8000/admin/logout/")

