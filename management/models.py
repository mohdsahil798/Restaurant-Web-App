from django.db import models

class Reservation(models.Model):
    PEOPLE_CHOICES = [(i, str(i)) for i in range(1, 7)]
    
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    date_time = models.DateTimeField(null=True, blank=True)
    number_of_people = models.IntegerField(default=1, choices=PEOPLE_CHOICES)
    special_request = models.TextField(null=True, blank=True)
    is_accepted = models.BooleanField(default=False)
    is_complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.name} - {self.date_time}"
    
    