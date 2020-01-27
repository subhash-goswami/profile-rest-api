from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API view"""
    def get(self,request, format=None):   # format set default return such as json ,text etc
        """Return a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to traditional Django View',
            'Gives you the most control over you application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message':'Hello!','an_apiview': an_apiview})


# Create your views here.
#
# def display_name(request, aid):  # aid is an perameter that is get from url
#     return HttpResponse("Subhash Hello world {}".format(aid))
#
#
# # To display template's html files
# def hello(request):
#     return render(request, "hello.html")
