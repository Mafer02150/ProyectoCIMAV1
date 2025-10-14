from django.shortcuts import render

# Create your views here.
def inscripcion(request):
    return render(request, 'inscripcion.html')