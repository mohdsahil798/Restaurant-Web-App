from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Reservation
from .serializers import ReservationSerializer

class ReservationAPIView(APIView):
    
    def get(self, request, *args, **kwargs):
        filters = {}
        if "is_complete" in request.GET:
            print("Is Complete", request.GET.get("is_complete"))
            filters["is_complete"] = request.GET.get("is_complete").lower() == "true"
        if "is_accepted" in request.GET:
            filters["is_accepted"] = request.GET.get("is_accepted").lower() == "true"
        print("Filters", filters)
        query_set = Reservation.objects.filter(**filters)
        
        sort_by = request.GET.get("sort_by")
        if sort_by:
            query_set = query_set.order_by(sort_by)
        
        serializer = ReservationSerializer(query_set, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        if isinstance(request.data, list):
            serializer = ReservationSerializer(data = request.data, many=True)
        else:
            serializer = ReservationSerializer(data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status = 400)
    
    def delete(self, request, pk, *args, **kwargs):
        try:
            reservation = Reservation.objects.get(pk=pk)
        except Reservation.DoesNotExist:
            return Response({"error":"Reservation Not Found"},status=404)
        reservation.delete()
        return Response({"message":"Reservation deleted successfully"},status=204)