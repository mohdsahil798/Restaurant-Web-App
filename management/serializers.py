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
        fields = [
            "meal_category", "name", "price", "photos", 
            "description", "is_available", "created_at", "updated_at"
        ]
        
class MealCategoryWithDishesSerializer(serializers.ModelSerializer):
    dishes = serializers.SerializerMethodField()
    
    class Meta:
        model = MealCategory
        fields = ["prefix", "ico_type", "name", "created_at", "updated_at",  "is_available", "dishes"]
        
        
    def get_dishes(self, obj):
        dishes = Dish.objects.filter(meal_category = obj)
        return DishSerializer(dishes, many = True).data