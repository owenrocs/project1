from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def nueva():
    return 0

def index(request):
    #return HttpResponse("Bienvenido :)")
    return render(request, 'index.html')

def procesamiento(request):
    nombre = request.POST['nombre']
    nombre = nombre.upper()
    return render(request, 'procesamiento.html', {'nombre': nombre})