from django.http import HttpResponse
# Create your views here.

def display_name(request):
    return HttpResponse("Subhash Hello world")
