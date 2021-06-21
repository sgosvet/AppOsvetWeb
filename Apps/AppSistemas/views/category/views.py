from Apps.AppSistemas.forms import CategoryForm
from Apps.AppSistemas.models import Category
from Apps.AppSistemas.mixins import ValidatePermissionRequiredMixin

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, FormView

# Pruebas de vistas basadas en CLASES

class CategoryListView(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):
    model = Category
    template_name = 'category/list.html'
    permission_required = 'AppSistemas.view_category'
    
    # El método dispatch se ejecuta al comienzo, cuando se hace una llamada a la vista.
    # Se encarga de redireccionar los métodos POST/GET dependiento la petición que se haga
    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        # Puedo configurar una acción dependiendo del request.method
        # if request.method == 'GET':
        #     return redirect('category_list')
        return super().dispatch(request, *args, **kwargs)
     
    # # Para modificar/validar los datos que enviamos a las plantillas
    # se utiliza el procedimiento get_queryset()
    # def get_queryset(self):
    #     return Category.objects.filter(name__icontains='t')
    
    # Para enviarle más parámetros a la plantilla (html), 
    # se sobreescribirá el procedimiento get_context_data()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Categorías'
        context['create_url'] = reverse_lazy('category_create')
        context['list_url'] = reverse_lazy('category_list')
        context['entity'] = 'Categorias'
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
                for i in Category.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
            # Busco el id de la categoría enviada por POST
            # Ejecuto el método del modelo .toJSON() para obtener todos los campos en ese formato
            # data = Category.objects.get(pk=request.POST['id']).toJSON()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False) #Cuando trabajamos con colecciones de dicts ([1,2,3]), usamos safe=False 
    
class CategoryCreateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category/create.html'
    success_url = reverse_lazy('category_list')
    permission_required = 'AppSistemas.add_category'
    url_redirect = success_url

    # @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        # self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)
    
    
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación una Categoria'
        context['entity'] = 'Categorias'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context

class CategoryUpdateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category/create.html'
    success_url = reverse_lazy('category_list')
    permission_required = 'AppSistemas.change_category'
    url_redirect = success_url


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
        context['title'] = 'Edición una Categoria'
        context['entity'] = 'Categorias'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        context["submitTitle"] = "Actualizar nueva categoría"
        return context

class CategoryDeleteView(LoginRequiredMixin, ValidatePermissionRequiredMixin, DeleteView):
    model = Category
    template_name = 'category/delete.html'
    success_url = reverse_lazy('category_list')
    permission_required = 'AppSistemas.delete_category'
    url_redirect = success_url

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
        context['title'] = 'Eliminar una Categoria'
        context['entity'] = 'Categorias'
        context['list_url'] = self.success_url
        context["submitTitle"] = "Sí, Eliminar categoría"
        return context
    
class CategoryFormView(FormView):
    # Clase que verifica que el formulario sea válido, y redirecciona a la url de success
    form_class = CategoryForm
    template_name = 'category/create.html'
    success_url = reverse_lazy('category_list')
    
    def form_valid(self, form):
        print(form)
        print(form.is_valid())
        return super().form_valid(form)
    
    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Form | Categoria'
        context['entity'] = 'Categorias'
        context['list_url'] = reverse_lazy('category_list')
        context['action'] = 'add'
        context["submitTitle"] = "Crear nueva categoría"
        return context    