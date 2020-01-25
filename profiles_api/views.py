from django.http import HttpResponse
# Create your views here.

def display_name(request,aid):
    return HttpResponse("Subhash Hello world {}".format(aid))
