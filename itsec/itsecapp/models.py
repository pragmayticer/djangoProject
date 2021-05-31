from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class RFID_Daten(models.Model):
    RFID_Id = models.CharField(max_length=256, null=False, blank=False)
    name = models.CharField(max_length=32, null=False, blank=False)
    login = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)