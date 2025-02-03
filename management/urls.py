from django.urls import path
from .views import *

urlpatterns = [
    path('api/reservations/', ReservationAPIView.as_view()),
    path('api/reservations/<int:pk>', ReservationAPIView.as_view()),
    
    path('api/meal-categories/', MealCategoryList.as_view(), name = "meal-category-list"),
    path('api/meal-categories/<int:pk>/', MealCategoryDetail.as_view(), name = "meal-category-list"),
]
