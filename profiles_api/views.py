from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):

    def get(self, request, format=None):
        an_apiview=[
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to traditional Django View',
            'Is mapped manually to URLs'
        ]

        return Response({
            'message': 'Test Message',
            'an_apiview': an_apiview
        })
