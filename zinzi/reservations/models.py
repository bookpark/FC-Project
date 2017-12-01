from django.db import models

from members.models import User
from restaurants.models import ReservationInfo


# fixme
class Reservation(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
    )
    information = models.ForeignKey(
        ReservationInfo,
        on_delete=models.PROTECT,
    )
    requested_date = models.DateTimeField(
        auto_now_add=True,
    )
    reserved_date = models.DateTimeField()
    payment_date = models.DateTimeField()
    price = models.PositiveIntegerField()
    party = models.PositiveIntegerField()
    reservation_number = models.PositiveIntegerField(
        unique=True,
    )
    is_confirmed = models.BooleanField(
        default=False,
    )


class TestModel(models.Model):
    imp_uid = models.TextField()
