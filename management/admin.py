from django.contrib import admin
from .models import *

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('name', 'mobile', 'date_time', 'number_of_people', 'is_accepted', 'is_complete', 'created_at')
    list_filter = ('is_accepted', 'is_complete', 'date_time', 'number_of_people')
    search_fields = ('name', 'mobile')
    list_editable = ('is_accepted', 'is_complete')
    ordering = ('-created_at',)
    date_hierarchy = 'date_time'

@admin.register(MealCategory)
class MealCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'prefix', 'is_available')
    list_filter = ('is_available',)
    search_fields = ('name', 'prefix')
    list_editable = ('is_available',)
    
@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('name', 'meal_category', 'price', 'is_available')
    list_filter = ('is_available', "meal_category")
    search_fields = ('name', 'description')
    list_editable = ('is_available',)

@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'message')
    search_fields = ('name', 'subject', 'message')
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'