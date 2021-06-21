from django.shortcuts import render, HttpResponse

# Create your views here.

def menuComercial(request):
    context = dict(request.session)
    return render(request, 'AppComercial/mnuComercial.html', context)

def mnuItem1(request):
    return render(request, 'AppComercial/item1.html')

def mnuItem2(request):
    return render(request, 'AppComercial/item2.html')

def mnuItem3(request):
    return render(request, 'AppComercial/item3.html')