from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.

def openTestHTML(request):
    context = dict(request.session)
    return render(request, 'develop/test.html', context)

# def menuSistemasItem2(request):
#     context = dict(request.session)
#     return render(request, 'AppSistemas/item2.html')

# def menuSistemasItem3(request):
#     context = dict(request.session)
#     return render(request, 'AppSistemas/item3.html')
