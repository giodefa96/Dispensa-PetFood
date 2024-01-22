from django.db import models

class Clinic(models.Model):
    clinic_name = models.CharField(max_length=200, blank=True)
    clinic_address = models.CharField(max_length=200, blank=True)
    clinic_phone = models.CharField(max_length=200, blank=True)
    clinic_email = models.CharField(max_length=200, blank=True)
    clinic_website = models.CharField(max_length=200, blank=True)
    clinic_description = models.TextField(blank=True)
    clinic_logo = models.ImageField(upload_to='clinic_logo', blank=True, null=True)


class OpeningHours(models.Model):
    DAYS_OF_WEEK = [
        ('monday', 'Monday'),
        ('tuesday', 'Tuesday'),
        ('wednesday', 'Wednesday'),
        ('thursday', 'Thursday'),
        ('friday', 'Friday'),
        ('saturday', 'Saturday'),
        ('sunday', 'Sunday'),
    ]

    clinic_id = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    day = models.CharField(max_length=200, choices=DAYS_OF_WEEK)
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
