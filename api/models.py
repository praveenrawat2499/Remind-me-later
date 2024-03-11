from django.db import models

class Alerts(models.Model):
    alert_date = models.DateField()
    alert_time = models.TimeField()
    alert_message = models.TextField() 