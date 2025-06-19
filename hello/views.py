from django.http import HttpResponse

# Home page view
def index(request):
    return HttpResponse("Hello from Roshitha, Rushitha, Harini!")
