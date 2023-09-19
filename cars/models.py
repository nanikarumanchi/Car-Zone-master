from django.db import models
from django.urls import reverse

from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField

from .constants import state_choice, year_choice, features_choices, door_choices


class Car(models.Model):
    title = models.CharField(max_length=256)
    state = models.CharField(choices=state_choice, max_length=4)
    city = models.CharField(max_length=128)
    color = models.CharField(max_length=128)
    model = models.CharField(max_length=128)
    year = models.IntegerField(choices=year_choice)
    condition = models.CharField(max_length=128)
    price = models.DecimalField(decimal_places=2, max_digits=16)
    description = RichTextField()
    car_photo = models.ImageField('Featured Image', upload_to='cars/%Y/%m/%d/')
    car_photo_1 = models.ImageField(
        upload_to='cars/%Y/%m/%d/', null=True, blank=True)
    car_photo_2 = models.ImageField(
        upload_to='cars/%Y/%m/%d/', null=True, blank=True)
    car_photo_3 = models.ImageField(
        upload_to='cars/%Y/%m/%d/', null=True, blank=True)
    car_photo_4 = models.ImageField(
        upload_to='cars/%Y/%m/%d/', null=True, blank=True)
    features = MultiSelectField(choices=features_choices)
    body_style = models.CharField(max_length=128)
    engine = models.CharField(max_length=128)
    transmission = models.CharField(max_length=128)
    interior = models.CharField(max_length=128)
    miles = models.DecimalField(decimal_places=2, max_digits=16)
    doors = models.CharField(max_length=128, choices=door_choices)
    passengers = models.IntegerField()
    vin_no = models.CharField(max_length=128)
    fule_type = models.CharField(max_length=128)
    no_of_owners = models.CharField(max_length=128)
    is_featured = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now=True)
    updated_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("cars:detail", kwargs={"id": self.id})
