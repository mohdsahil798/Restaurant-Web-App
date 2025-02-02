from django.shortcuts import render, redirect
from django.contrib import messages
from management.models import *
from datetime import datetime
from django.http import JsonResponse


def home(request):
    categories = MealCategory.objects.filter(is_available=True)
    dishes_by_category = {}

    for category in categories:
        dishes = Dish.objects.filter(meal_category=category, is_available=True)
        dishes_by_category[category] = dishes

    context = {
        'categories': categories,
        'dishes_by_category': dishes_by_category,
    }
    if request.method == 'POST':
        try:
            # Create new reservation
            reservation = Reservation(
                name=request.POST['name'],
                mobile=request.POST['mobile'],
                date_time=request.POST['date_time'],
                number_of_people=request.POST['number_of_people'],
                special_request=request.POST['special_request']
            )
            reservation.save()
            context.update({
                'status': 'success',
                'message': 'Reservation submitted successfully! We will contact you soon.'
            })
            return render(request, 'index.html', context)

        except Exception as e:
            context.update({
                'status': 'error',
                'message': 'There was an error processing your reservation. Please try again.'
            })
            return render(request, 'index.html', context)

    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')


def service(request):
    return render(request, 'service.html')


def menu(request):
    categories = MealCategory.objects.filter(is_available=True)
    dishes_by_category = {}

    for category in categories:
        dishes = Dish.objects.filter(meal_category=category, is_available=True)
        dishes_by_category[category] = dishes

    context = {
        'categories': categories,
        'dishes_by_category': dishes_by_category,
    }
    return render(request, 'menu.html', context)


def contact(request):
    if request.method == 'POST':
        contact = ContactUs(
            name=request.POST.get('name'),
            mobile=request.POST.get('mobile'),
            subject=request.POST.get('subject'),
            message=request.POST.get('message')
        )
        contact.save()

    return render(request, 'contact.html')
