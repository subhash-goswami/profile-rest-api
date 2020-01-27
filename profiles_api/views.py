from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def display_name(request, aid):  # aid is an perameter that is get from url
    return HttpResponse("Subhash Hello world {}".format(aid))


# To display template's html files
def hello(request):
    return render(request, "hello.html")
