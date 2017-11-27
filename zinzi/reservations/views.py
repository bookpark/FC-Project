from datetime import datetime

from django.shortcuts import get_object_or_404, redirect

from restaurants.models import ReservationInfo
from .models import Reservation


def reserve(request, info_pk):
    user = request.user
    information = get_object_or_404(ReservationInfo, pk=info_pk)
    date = information.date
    reserved_date = datetime(date.year, date.month, date.day, information.time.hour)
    payment_date = datetime.now()
    price = 4000
    party = 4
    reservation_number = 1

    reservation = Reservation(user=user,
                              information=information,
                              reserved_date=reserved_date,
                              payment_date=payment_date,
                              price=price,
                              party=party,
                              reservation_number=reservation_number,
                              )
    reservation.save()
    return redirect('restaurant')


def reservation_complete(request, pk):
    reservation = get_object_or_404(
        Reservation,
        pk=pk
    )
    context = {
        'reservation': reservation
    }
    return render(request, 'reservations/complete.html', context)
