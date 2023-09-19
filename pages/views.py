from django.shortcuts import render

from teams.models import Team
from cars.models import Car


def home_page(request):
    teams = Team.objects.all()
    cars = Car.objects.all()
    featured_cars = cars.filter(is_featured=True).order_by('-created_date')
    latest_cars = cars[:2]
    search_fields = {
        'cities': list(set(cars.values_list('city', flat=True))),
        'models': list(set(cars.values_list('model', flat=True))),
        'years':  list(set(cars.values_list('year', flat=True))),
        'body_styles': list(set(cars.values_list('body_style', flat=True))),
    }
    context = {
        'teams': teams,
        'featured_cars': featured_cars,
        'latest_cars': latest_cars,
        'search_fields': search_fields
    }
    return render(request, 'pages/home.html', context)


def about_page(request):
    teams = Team.objects.all()
    context = {
        'teams': teams
    }
    return render(request, 'pages/about.html', context)


def services_page(request):
    return render(request, 'pages/services.html')


def contact_page(request):
    return render(request, 'pages/contact.html')
