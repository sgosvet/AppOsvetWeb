from Apps.AppSistemas.forms import ZonasForm
from Apps.AppSistemas.models import Zonas
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, FormView

# Pruebas de vistas basadas en CLASES

class ZonasListView(ListView):
    model = Zonas
    template_name = 'zonas/list.html'
    
    # El método dispatch se ejecuta al comienzo, cuando se hace una llamada a la vista.
    # Se encarga de redireccionar los métodos POST/GET dependiento la petición que se haga
    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        # Puedo configurar una acción dependiendo del request.method
        # if request.method == 'GET':
        #     return redirect('zonas_list')
        return super().dispatch(request, *args, **kwargs)
     
    # # Para modificar/validar los datos que enviamos a las plantillas
    # se utiliza el procedimiento get_queryset()
    # def get_queryset(self):
    #     return Category.objects.filter(name__icontains='t')
    
    # Para enviarle más parámetros a la plantilla (html), 
    # se sobreescribirá el procedimiento get_context_data()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Listado de Zonas"
        context["create_url"] = reverse_lazy('zonas_create')
        
        return context

    # Sobrescribir el método POST
    def post(self, request, *args, **kwargs):
        data = {}
        # Procedimiento para atrapar el error
        try:
            # Cargar datos en mi tabla con ajax y datatable
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Zonas.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
            # Busco el id de la categoría enviada por POST
            # Ejecuto el método del modelo .toJSON() para obtener todos los campos en ese formato
            # data = Category.objects.get(pk=request.POST['id']).toJSON()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False) #Cuando trabajamos con colecciones de dicts ([1,2,3]), usamos safe=False 
    
class ZonasCreateView(CreateView):
    model = Zonas
    form_class = ZonasForm
    template_name = 'zonas/create.html'
    success_url = reverse_lazy('zonas_list')

    # @method_decorator(login_required) 
    # def dispatch(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #     return super().dispatch(request, *args, **kwargs)
    
    
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = '[CREATE] No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    #     print(request.POST)
    #     form = CategoryForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return HttpResponseRedirect(self.success_url)
    #     self.object = None
    #     context = self.get_context_data(**kwargs)
    #     context['form'] = form
    #     return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación una Zona'
        context['entity'] = 'Zonas'
        context['list_url'] = reverse_lazy('zonas_list')
        context['action'] = 'add'
        context["submitTitle"] = "Crear nueva zona"
        return context

class ZonasUpdateView(UpdateView):
    model = Zonas
    form_class = ZonasForm
    template_name = 'zonas/create.html'
    success_url = reverse_lazy('zonas_list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = '[UPDATE] No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición una Zona'
        context['entity'] = 'Zonas'
        context['list_url'] = reverse_lazy('zonas_list')
        context['action'] = 'edit'
        context["submitTitle"] = "Actualizar nueva zona"
        return context

class ZonasDeleteView(DeleteView):
    model = Zonas
    template_name = "zonas/delete.html"
    success_url = reverse_lazy("zonas_list")


    @method_decorator(login_required) 
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar una zona'
        context['entity'] = 'Zonas'
        context['list_url'] = reverse_lazy('zonas_list')
        # context['action'] = 'edit' --> No se envía 'action' porque no se usa ajax
        context["submitTitle"] = "Sí, Eliminar zona"
        return context
    
class ZonasFormView(FormView):
    # Clase que verifica que el formulario sea válido, y redirecciona a la url de success
    form_class = ZonasForm
    template_name = 'zonas/create.html'
    success_url = reverse_lazy('zonas_list')
    
    def form_valid(self, form):
        print(form)
        print(form.is_valid())
        return super().form_valid(form)
    
    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Form | Zona'
        context['entity'] = 'Zonas'
        context['list_url'] = reverse_lazy('zonas_list')
        context['action'] = 'add'
        context["submitTitle"] = "Crear nueva zona"
        return context    