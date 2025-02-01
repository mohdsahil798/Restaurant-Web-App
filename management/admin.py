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
