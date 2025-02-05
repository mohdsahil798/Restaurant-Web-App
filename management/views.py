from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Reservation, MealCategory, Dish
from .serializers import ReservationSerializer, MealCategorySerializer, DishSerializer, MealCategoryWithDishesSerializer
from django.db.models import Prefetch

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
    
    def put(self, request, pk, *args, **kwargs):
        try:
            reservation = Reservation.objects.get(pk=pk)
        except Reservation.DoesNotExist:
            return Response({"error":"Reservation Not Found"},status=404)
        
        serializer = ReservationSerializer(reservation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    def patch(self,request, pk, *args, **kwargs):
        try:
            reservation = Reservation.objects.get(pk=pk)
        except Reservation.DoesNotExist:
            return Response({"error":"Reservation Not Found"},status=404)
        
        serializer = ReservationSerializer(reservation, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    
class MealCategoryList(APIView):
    def get(self, request):
        categories = MealCategory.objects.all()
        serializer = MealCategorySerializer(categories, many = True)
        return Response(serializer.data, status=200)
    
    def post(self, request):
        serializer = MealCategorySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
class MealCategoryDetail(APIView):
    def get_object(self, pk):
        try:
            return MealCategory.objects.get(pk=pk)
        except MealCategory.DoesNotExist:
            return None
        
    def get(self, request, pk):
        category = self.get_object(pk)
        if category is None:
            return Response({"error":"Category Not Found"},status=404)
        serializer = MealCategorySerializer(category)
        return Response(serializer.data, status=200)
    
    def put(self, request, pk):
        category = self.get_object(pk)
        if category is not None:
            serializer = MealCategorySerializer(category, data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
        return Response({"error":"category not found"}, status=404)
    
    def patch(self, request, pk):
        category = self.get_object(pk)
        if category is not None:
            serializer = MealCategorySerializer(category, data = request.data, partial = True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
        return Response({"error":"category not found"}, status=404)
    
    def delete(self, request, pk):
        category = self.get_object(pk)
        if category is not None:
            category.delete()
            return Response({"message":"Category deleted successfully"}, status=204)
        return Response({"error":"Category not found"}, status=404)

class DishList(APIView):
    def get(self, request):
        dishes = Dish.objects.all()
        serializer = DishSerializer(dishes, many = True)
        return Response(serializer.data, status=200)
    
    def post(self, request):
        serializer = DishSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
class DishDetail(APIView):
    def get_object(self, pk):
        try:
            return Dish.objects.get(pk=pk)
        except Dish.DoesNotExist:
            return None
    
    def get(self, request, pk):
        dish = self.get_object(pk)
        if dish is None:
            return Response({"error":"Dish Not Found"},status=404)
        serializer = DishSerializer(dish)
        return Response(serializer.data, status=200)
    
    def put(self, request, pk):
        dish = self.get_object(pk)
        if dish is not None:
            serializer = DishSerializer(dish, data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
        return Response({"error":"Dish not found"}, status=404)
    
    def patch(self, request, pk):
        dish = self.get_object(pk)
        if dish is not None:
            serializer = DishSerializer(dish, data = request.data, partial = True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
        return Response({"error":"Dish not found"}, status=404)
    
    def delete(self, request, pk):
        dish = self.get_object(pk)
        if dish is not None:
            dish.delete()
            return Response({"message":"Dish deleted successfully"}, status=204)
        return Response({"error":"Dish not found"}, status=404)
    
class MealCategoryWithDishesList(APIView):
    def get(self, request):
        categories = MealCategory.objects.prefetch_related(
            Prefetch('dish_set', queryset=Dish.objects.all())
        )
        print(categories.values())
        serializer = MealCategoryWithDishesSerializer(categories, many = True)
        return Response(serializer.data)

