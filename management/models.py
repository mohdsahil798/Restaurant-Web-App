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
    
class MealCategory(models.Model):
    prefix = models.CharField(max_length=128, blank=True, null=True)
    name = models.CharField(max_length=100)
    ico_type = models.CharField(max_length=128, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_available = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
class Dish(models.Model):
    meal_category = models.ForeignKey(MealCategory, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    photos = models.ImageField(upload_to='dishes_photos/', blank=True, null=True)
    description = models.CharField(max_length=150, null=True, blank=True)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=13)
    subject = models.CharField(max_length=256)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.DateField(auto_now=True)
    