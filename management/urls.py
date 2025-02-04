from django.urls import path
from .views import *

urlpatterns = [
    path('api/reservations/', ReservationAPIView.as_view()),
    path('api/reservations/<int:pk>', ReservationAPIView.as_view()),
    
    path('api/meal-categories/', MealCategoryList.as_view(), name = "meal-category-list"),
    path('api/meal-categories/<int:pk>/', MealCategoryDetail.as_view(), name = "meal-category-detail"),
    
    path('api/dish/', DishList.as_view(), name = "dish-list"),
    path('api/dish/<int:pk>/', DishDetail.as_view(), name = "dish-detail"),
    
    path('api/meal-categories-with-dishes/', MealCategoryWithDishesList.as_view()),
]
