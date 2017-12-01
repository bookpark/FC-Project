from django.shortcuts import render
from iamport import Iamport
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from reservations.serializers import TestSerializer


def test(request):
    return render(request, 'test.html')


class TestList(APIView):
    def post(self, request):
        iamport = Iamport(imp_key='6343293486082258',
                          imp_secret='JEAB6oXOMsc2oysgdu4tJzlfgQvn5sfP7Qqefn21Qe3fNwv11zuL9Q0qGvNMY2B6T1l8pn9fCdvpK0rL')
        response = iamport.find(imp_uid=request.data.get('test_field'))
        serializer = TestSerializer(data=response)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
