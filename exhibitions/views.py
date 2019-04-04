from rest_framework import status as HttpStatus
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


class HelloWorldApiView(APIView):

    def get(self, request, format=None):
        return Response({'message': 'Hello World!!!'})
