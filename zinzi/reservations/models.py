from django.db import models

from accounts.models import User
from restaurants.models import ReservationInfo, Restaurant


class Reservation(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
    )
    information = models.ForeignKey(
        ReservationInfo,
        on_delete=models.PROTECT,
    )
    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.PROTECT,
    )
    name = models.CharField(max_length=10, blank=True, null=True)
    party = models.PositiveSmallIntegerField()
    price = models.PositiveIntegerField()
    phone_number = models.CharField(max_length=11, blank=True, null=True)
    email = models.CharField(max_length=30, blank=True, null=True)
    status = models.CharField(max_length=10, default='paid')

    def __str__(self):
        return f'reservation_pk:{self.pk} information_pk{self.information.pk}'


class Payment(models.Model):
    # 고유번호
    imp_uid = models.CharField(max_length=50)
    merchant_uid = models.CharField(max_length=50)
    # 지불방법 및 pg사 정보
    pay_method = models.CharField(max_length=20)
    pg_provider = models.CharField(max_length=20)
    pg_tid = models.CharField(max_length=50)
    # 주문정보
    name = models.CharField(max_length=50)
    amount = models.IntegerField()
    cancel_amount = models.IntegerField()
    currency = models.CharField(max_length=5)
    status = models.CharField(max_length=10)
    paid_at = models.IntegerField()
    failed_at = models.IntegerField()
    cancelled_at = models.IntegerField()
    fail_reason = models.CharField(max_length=255, null=True, blank=True)
    cancel_reason = models.CharField(max_length=255, null=True, blank=True)
    # 주문자 정보
    buyer_name = models.CharField(max_length=10)
    buyer_email = models.CharField(max_length=30)
    buyer_tel = models.CharField(max_length=20)
    # Reservation 모델 연결
    reservation = models.OneToOneField(
        Reservation,
        on_delete=models.PROTECT,
    )

    def __str__(self):
        return f'payment_pk:{self.pk} reservation_pk:{self.reservation.pk}'


class PaymentCancel(models.Model):
    payment = models.OneToOneField(
        Payment,
        on_delete=models.CASCADE,
    )
    reason = models.CharField(max_length=50)
