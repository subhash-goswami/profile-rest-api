from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import serializers

class HelloApiView(APIView):
    """Test API view"""
    serializer_class=serializers.HelloSerializer

    def get(self,request, format=None):   # format set default return such as json ,text etc
        """Return a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to traditional Django View',
            'Gives you the most control over you application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message':'Hello!','an_apiview': an_apiview}, status=200)

    def post(self, request):
        """Creating hello message with name """
        serializer=self.serializer_class(data=request.data)

        # now check valid data
        if serializer.is_valid():
            name = serializer.validated_data.get('name')  # get name value
            return Response({
                'message': 'Hello {}'.format(name)
            },status=200)
        return Response(serializer.errors, status=400)  # Bad Request

    def put(self,request, pk=None):  # pk=None is represent that we are not send primary key in put methods
        """handle updating an object"""
        return Response({'method':'PUT'},status=200)

    def patch(self,request, pk=None):  # patch is used for update particular field in tables
        """Handle a partial update of an object"""
        return Response({'method': 'PATCH'}, status=200)

    def delete(self,request, pk=None):
        """Delete an object"""
        return Response({'method':'DELETE'})
# Create your views here.
#
# def display_name(request, aid):  # aid is an perameter that is get from url
#     return HttpResponse("Subhash Hello world {}".format(aid))
#
#
# # To display template's html files
# def hello(request):
#     return render(request, "hello.html")
