from rest_framework import serializers
from .models import Reservation, MealCategory, Dish

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = "__all__"
    
class MealCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MealCategory
        fields = "__all__"
        
class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = "__all__"