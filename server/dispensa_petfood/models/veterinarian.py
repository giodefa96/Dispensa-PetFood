from django.db import models


class Veterinarian(models.Model):
    veterinarian_name = models.CharField(max_length=200, blank=True)
    clinic_id = models.ForeignKey('clinic.Clinic', on_delete=models.CASCADE)
    veterinarian_address = models.CharField(max_length=200, blank=True)
    veterinarian_phone = models.CharField(max_length=200, blank=True)
    veterinarian_email = models.CharField(max_length=200, blank=True)
    veterinarian_website = models.CharField(max_length=200, blank=True)
    veterinarian_description = models.TextField(blank=True)
    
    
class VeterinarianSchedule(models.Model):
    DAYS_OF_WEEK = [
        ('monday', 'Monday'),
        ('tuesday', 'Tuesday'),
        ('wednesday', 'Wednesday'),
        ('thursday', 'Thursday'),
        ('friday', 'Friday'),
        ('saturday', 'Saturday'),
        ('sunday', 'Sunday'),
    ]

    veterinarian_id = models.ForeignKey(Veterinarian, on_delete=models.CASCADE)
    day = models.CharField(max_length=200, choices=DAYS_OF_WEEK)
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)