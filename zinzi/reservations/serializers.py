from rest_framework import serializers

from reservations.models import TestModel


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestModel
        fields = (
            'imp_uid',
        )
