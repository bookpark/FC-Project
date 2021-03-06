from rest_framework import serializers

from reservations.models import Payment, PaymentCancel
from reservations.serializers import ReservationSerializer


class PaymentSerializer(serializers.ModelSerializer):
    reservation = ReservationSerializer(read_only=True)

    class Meta:
        model = Payment
        fields = (
            'pk',
            'imp_uid',
            'merchant_uid',
            'pay_method',
            'pg_provider',
            'pg_tid',
            'name',
            'amount',
            'cancel_amount',
            'currency',
            'status',
            'paid_at',
            'failed_at',
            'cancelled_at',
            'fail_reason',
            'cancel_reason',
            'buyer_name',
            'buyer_email',
            'buyer_tel',
            'reservation',
        )


class PaymentNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = (
            'imp_uid',
            'merchant_uid',
        )


class PaymentCancelSerializer(serializers.ModelSerializer):
    payment = PaymentNumberSerializer(read_only=True)

    class Meta:
        model = PaymentCancel
        fields = (
            'pk',
            'reason',
            'payment',
        )
