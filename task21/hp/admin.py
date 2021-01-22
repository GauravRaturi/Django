from django.contrib import admin
from .models import notification
# Register your models here.

@admin.register(notification)
class notificationAdmin(admin.ModelAdmin):    
    list_display = ['id', 'name', 'notification_type', 'notified_person', 'notification_status', 'created_at', 'updated_at', 'deleted_at', 'is_active', 'is_deleted']
