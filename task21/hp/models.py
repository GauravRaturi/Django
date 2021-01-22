from django.db import models
from django.utils import timezone

class notification(models.Model):
    name = models.CharField(max_length=50)
    notification_type = models.CharField(max_length=50)
    notified_person = models.CharField(max_length=50)
    notification_status = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)


