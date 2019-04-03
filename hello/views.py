from django.shortcuts import HttpResponse

# Create your views here.
def hello_world(request):
    return HttpResponse("<h1>Hello world !</h1>")