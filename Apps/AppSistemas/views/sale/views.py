from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView

from Apps.AppSistemas.forms import SaleForm
from Apps.AppSistemas.models import Product, Sale
from Apps.AppSistemas.mixins import ValidatePermissionRequiredMixin

class SaleCreateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
    model = Sale
    form_class = SaleForm
    template_name = 'sale/create.html'
    success_url = reverse_lazy('index')
    permission_required = 'AppSistemas.add_sale'
    url_redirect = success_url

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'search_products':
                data = []
                prods = Product.objects.filter(name__startswith=request.POST['term'])
                # prods = Product.objects.all()
                for i in prods:
                    item = i.toJSON()
                    item['value'] = i.name
                data.append(item)
            else:
                data['error'] = 'No ha ingresado a ninguna opción para '+action
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False) 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de una venta'
        context['entity'] = 'Ventas'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context

