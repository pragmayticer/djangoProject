from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User,AnonymousUser
from .models import RFID_Daten

from django.contrib.auth.decorators import login_required
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from datetime import datetime
import time
import random

GPIO.setwarnings(False)
reader = SimpleMFRC522()

def home_view(request):
    rfid_id: int = 0
    rfid_id, text = reader.read()
    print(reader.read())
    GPIO.cleanup()
    if request.user.is_anonymous:
        return render(request, "./base.html")
    current_usermail = request.user.email
    current_user = User.objects.get(email=current_usermail)
    all_RFID_Daten: QuerySet=RFID_Daten.objects.filter(user=current_user)
    if current_user.is_superuser:
        current_RFID = int(all_RFID_Daten[0].RFID_Id)
        if current_RFID == rfid_id:
            all_RFID_Daten: QuerySet=RFID_Daten.objects.all()
            b = RFID_Daten(RFID_Id=current_RFID, name=current_user.username, login=datetime.now(), user=current_user)
            b.save()
            return render(request, "./base.html", {'posts': all_RFID_Daten})
    else:
        current_RFID = int(all_RFID_Daten[0].RFID_Id)
        if rfid_id == current_RFID:
            b = RFID_Daten(RFID_Id=current_RFID, name=current_user.username, login=datetime.now(), user=current_user)
            b.save()
            return render(request, "./base.html", {'posts': all_RFID_Daten})
        else:
            return HttpResponse("Kein Zugriff möglich")
    return HttpResponse("Kein Zugriff möglich")
# def home_view(request):
#     rfid_id: int = 0
#     rfid_id, text = reader.read()
#     print(reader.read())
#     GPIO.cleanup()
#     if request.user.is_anonymous:
#         return render(request, "./base.html")
#     current_usermail = request.user.email
#     current_user = User.objects.get(email=current_usermail)
#     all_RFID_Daten: QuerySet=RFID_Daten.objects.filter(user=current_user)
#     if current_user.is_superuser:
#         current_RFID = int(all_RFID_Daten[0].RFID_Id)
# 
#         all_RFID_Daten: QuerySet=RFID_Daten.objects.all()
#         b = RFID_Daten(RFID_Id=current_RFID, name=current_user.username, login=datetime.now(), user=current_user)
#         b.save()
#         return render(request, "./base.html", {'posts': all_RFID_Daten})
#     else:
#         current_RFID = int(all_RFID_Daten[0].RFID_Id)
#         
#         b = RFID_Daten(RFID_Id=current_RFID, name=current_user.username, login=datetime.now(), user=current_user)
#         b.save()
#         return render(request, "./base.html", {'posts': all_RFID_Daten})
#     return HttpResponse("Kein Zugriff möglich")

def write_card(request):
    current_user= User.objects.get(email=request.user.email)
    if current_user.is_superuser:
        newest_user=User.objects.order_by('-date_joined')[0]
        print("neue user",newest_user)
        text = newest_user.username
        rfid_id = random.randint(1000,10000)
        print("rfid vor schleife",rfid_id)
        while True:
            try:
                RFID_Daten.objects.get(RFID_Id=rfid_id)
                rfid_id= random.randint(1000,10000)
                print("neu Werfeln",rfid_id)
            except RFID_Daten.DoesNotExist:
                print("Fehler breake")
                break
        b = RFID_Daten(RFID_Id=rfid_id, name=newest_user.username, login=datetime.now(), user=newest_user)
        b.save()
        print("Now place your tag to write")
        print(text)
        new_data = text+str(rfid_id) 
        reader.write(new_data)
        print("Written")
        GPIO.cleanup()
    else:
        return redirect("https://localhost:8000/admin/login/")
    return HttpResponse("Karte erfolgreich geschrieben")

def login_view(request):
    return redirect("https://localhost:8000/admin/login/")

def logout_view(request):
    return redirect("https://localhost:8000/admin/logout/")

