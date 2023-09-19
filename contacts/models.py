from datetime import datetime
from django.db import models
from django.contrib.auth import get_user_model


from cars.models import Car

User = get_user_model()
# Create your models here.


class Contact(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    car = models.ForeignKey(
        Car, related_name='car_enquiries', on_delete=models.CASCADE, null=True, blank=True)
    customer_need = models.CharField(max_length=256)
    city = models.CharField(max_length=256)
    state = models.CharField(max_length=256)
    email = models.EmailField(max_length=256)
    phone = models.CharField(max_length=16, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    user = models.ForeignKey(
        User, related_name='user_enquires', on_delete=models.CASCADE)
    created_at = models.DateTimeField(
        default=datetime.now, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} quires about {self.car.title}"
