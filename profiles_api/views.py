from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from . import models
from . import serializers
from . import permissions


class HelloApiView(APIView):
    """Test API view"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):  # format set default return such as json ,text etc
        """Return a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to traditional Django View',
            'Gives you the most control over you application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview}, status=200)

    def post(self, request):
        """Creating hello message with name """
        serializer = self.serializer_class(data=request.data)

        # now check valid data
        if serializer.is_valid():
            name = serializer.validated_data.get('name')  # get name value
            return Response({
                'message': 'Hello {}'.format(name)
            }, status=200)
        return Response(serializer.errors, status=400)  # Bad Request

    def put(self, request, pk=None):  # pk=None is represent that we are not send primary key in put methods
        """handle updating an object"""
        return Response({'method': 'PUT'}, status=200)

    def patch(self, request, pk=None):  # patch is used for update particular field in tables
        """Handle a partial update of an object"""
        return Response({'method': 'PATCH'}, status=200)

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test ViewSet"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a list of Hello message it is like get methods in APIView features"""
        a_viewset = [
            'Uses action (list, create, retrieve, update, partial_update)',
            'Application maps ot URLs using Routers',
            'Provides more functionality with less code',
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset}, status=200)

    def create(self, request):
        """Create a new Hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            return Response({'message': 'Hello {}'.format(name)}, status=200)
        return Response(
            serializer.errors,
            status=400
        )

    def retrieve(self, request, pk=None):
        """Handling getting an object by its ID"""
        return Response({"http_method": 'GET'}, status=200)

    def update(self, request, pk=None):
        """Handling updating an Object"""
        return Response({'http_method': "PUT"})

    def partial_update(self, request, pk=None):
        """Handling update part of an object"""
        return Response({'http_method': 'PATCH'}, status=200)

    def destroy(self, request, pk=None):
        """Handling Dele ting an object"""
        return Response({'http_method': 'DELETE'}, status=200)


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handling creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    # Through queryset.all() methods we copy all create, list, retrieve, update, partial_update, destroy etc
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email')


class Demo(viewsets.ModelViewSet):
    serializer_class = serializers.DemoSerializer
    queryset = models.Demo.objects.all()


class UserLoginApiView(ObtainAuthToken):
    """Handling user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

# Create your views here.
#
# def display_name(request, aid):  # aid is an perameter that is get from url
#     return HttpResponse("Subhash Hello world {}".format(aid))
#
#
# # To display template's html files
# def hello(request):
#     return render(request, "hello.html")
