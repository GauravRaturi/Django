from django.contrib import admin
from .models import Market
# Register your models here.
@admin.register(Market)
class MarketAdmin(admin.ModelAdmin):
 fields = ['product', 'name', 'notified_person', 'notification_status', 'size', 'address']
