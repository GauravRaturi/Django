from django.db import models
from django.utils import timezone


# Create your models here.
class Market(models.Model):
 product = models.CharField(max_length=50)
 name = models.CharField(max_length=50)
 notified_person = models.CharField(max_length=50)
 notification_status = models.CharField(max_length=50)
 size = models.IntegerField()
 address = models.CharField(max_length=50)
 #ordered_at = models.DateTimeField(default=timezone.now)
 #updated_at = models.DateTimeField(default=timezone.now)


