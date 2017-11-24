from django.shortcuts import render, get_object_or_404

from .models import Restaurant


def restaurant_list(request):
    restaurants = Restaurant.objects.all()

    ctx = {
        'restaurants': restaurants
    }
    return render(request, 'restaurants/list.html', ctx)


def restaurant_detail(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    reservationinfos = restaurant.tables.first().reservations.all()
    ctx = {
        'restaurant': restaurant,
        'reserv_infos': reservationinfos,
    }
    return render(request, 'restaurants/detail.html', ctx)