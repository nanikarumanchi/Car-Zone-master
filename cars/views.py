from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .models import Car
# Create your views here.


# def car_list(request):
#     cars = Car.objects.all()
#     context = {'cars': cars}
#     return render(request, 'cars/list.html', context)


class CarListView(ListView):
    queryset = Car.objects.all()
    context_object_name = 'cars'
    template_name = 'cars/list.html'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_fields = {
            'cities': list(set(self.queryset.values_list('city', flat=True))),
            'models': list(set(self.queryset.values_list('model', flat=True))),
            'years':  list(set(self.queryset.values_list('year', flat=True))),
            'body_styles': list(set(self.queryset.values_list('body_style', flat=True))),
        }
        context["search_fields"] = search_fields
        return context


@login_required
def car_detail(request, id):
    car = get_object_or_404(Car, pk=id)
    context = {'car': car}
    return render(request, 'cars/detail.html', context)


def search(request):
    query = request.GET.get('query')
    model_query = request.GET.get('select-model')
    city_query = request.GET.get('select-city')
    year_query = request.GET.get('select-year')
    body_query = request.GET.get('select-body')
    min_price_query = request.GET.get('min_price')
    max_price_query = request.GET.get('max_price')
    cars = Car.objects.all().order_by('-created_date')
    if query:
        look_up = (Q(title__icontains=query) |
                   Q(description__icontains=query))
        cars = cars.filter(look_up)
    if model_query:
        cars = cars.filter(model__iexact=model_query)
    if city_query:
        cars = cars.filter(city__iexact=city_query)
    if year_query:
        cars = cars.filter(year__iexact=year_query)
    if body_query:
        cars = cars.filter(body_style__iexact=body_query)
    if min_price_query:
        cars = cars.filter(price__gte=min_price_query)
    if max_price_query:
        cars = cars.filter(price__lte=max_price_query)
    context = {
        'cars': cars,
        'query': query,
    }
    return render(request, 'cars/search.html', context)
