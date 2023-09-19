from django.urls import path

from . import views

app_name = 'cars'

urlpatterns = [
    path('', views.CarListView.as_view(), name='list'),
    path('<int:id>/', views.car_detail, name='detail'),
    path('search/', views.search, name='search')
]
