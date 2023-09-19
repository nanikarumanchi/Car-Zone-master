from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.
from cars.models import Car
from .models import Contact
from django.core.mail import send_mail


def enquiry(request):
    if request.method == "POST":
        data = request.POST
        print(data)
        user = data.get("user")
        car = data.get("car")
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        customer_need = data.get("customer_need")
        city = data.get("city")
        state = data.get("state")
        email = data.get("email")
        phone = data.get("phone")
        message = data.get("message")
        car_obj = Car.objects.get(id=car)
        if user and car and first_name and last_name and city and state and customer_need and email:
            if Contact.objects.filter(car__id=car, user=request.user).exists():
                messages.success(
                    request, "Your Have Already Enquired about this CAR")
                return redirect('accounts_app:dashboard')
            Contact.objects.create(
                first_name=first_name, last_name=last_name, car=car_obj, customer_need=customer_need,
                city=city, state=state, email=email,
                phone=phone, message=message, user=request.user
            )
            messages.success(request, "Your Contact is ADDED")
            return redirect('accounts_app:dashboard')
        else:
            messages.error(request, "Some Enquiry Fields Are Missing")
            return redirect(car_obj.get_absolute_url())
    return redirect('accounts_app:dashboard')
