from django.contrib import admin
from .models import Alerts

@admin.register(Alerts)
class AlertsAdmin(admin.ModelAdmin):
    list_display = ['id','alert_date', 'alert_time', 'alert_message']
    
    def display_date(self, obj):
        return obj.date
    
    display_date.short_description = 'Date'
    
    def display_time(self, obj):
        return obj.time.strftime("%H:%M")
    
    display_time.short_description = 'Time'
