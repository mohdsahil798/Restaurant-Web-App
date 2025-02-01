from django.urls import path
from .views import *

urlpatterns = [
    path('api/reservations/', ReservationAPIView.as_view()),
    path('api/reservations/<int:pk>', ReservationAPIView.as_view())
]
