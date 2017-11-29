from django.shortcuts import render
from rest_framework import generics

from reservations.models import TestModel
from reservations.serializers import TestSerializer


def test(request):
    return render(request, 'test.html')


class TestList(generics.ListCreateAPIView):
    queryset = TestModel.objects.all()
    serializer_class = TestSerializer
