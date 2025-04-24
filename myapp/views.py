
from django.http import HttpResponse


# Create your views here.
def Login(request):
    return HttpResponse("<h1>D Y P</h1>")

def Diagnostico(request):
    return HttpResponse('<h1>Diagnostico</h1>')

def Historial(request):
    return HttpResponse('<h1>Historial de lesiones</h1>')