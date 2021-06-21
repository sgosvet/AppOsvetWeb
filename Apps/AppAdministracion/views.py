from django.shortcuts import render

# Create your views here.

def menuAdministracion(request):
    context = dict(request.session)
    return render(request, 'AppAdministracion/mnuAdministracion.html', context)

def menuAdmItem1(request):
    return render(request, 'AppAdministracion/item1.html')

def menuAdmItem2(request):
    return render(request, 'AppAdministracion/item2.html')

def menuAdmItem3(request):
    return render(request, 'AppAdministracion/item3.html')