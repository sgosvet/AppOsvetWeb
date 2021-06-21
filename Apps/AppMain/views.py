from django.shortcuts import render

# Create your views here.
def abrirIndex(request):
    return render(request, 'AppMain/body.html')