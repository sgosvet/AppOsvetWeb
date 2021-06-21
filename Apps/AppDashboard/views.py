from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

def dashSistemas(request):
    context = {
            'pagetitle':'DASHBOARD de Sistemas',
              }
    return render(request, 'AppDashboard/dsb_sistemas.html', context)

def dashAdministracion(request):
    context = dict(request.session)
    return render(request, 'AppDashboard/dsb_administracion.html', context)

def dashComercial(request):
    context = dict(request.session)
    return render(request, 'AppDashboard/dsb_comercial.html', context)

def dashOperaciones(request):
    context = dict(request.session)
    return render(request, 'AppDashboard/dsb_operaciones.html', context)

class DashboardView(TemplateView):
    template_name = "AppDashboard/dashboard.html"
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['panel'] = 'Panel del Administrador'
        return context
    
