from Apps.AppSistemas.forms import TestForm
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from Apps.AppSistemas.models import Product



class testView(TemplateView):
    template_name = "test.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Select Anidados | Django'
        context['form'] = TestForm()
        return context
    
    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'search_product_id':
                data = [{'id': '', 'text': '---------'}] # Enviamos una colección, no un diccionario
                for i in Product.objects.filter(cate_id=request.POST['id']):
                    data.append({'id': i.id, 'text': i.name, 'data': i.cate.toJSON()}) # Envia en 'data' toda la categoría completa
                
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

class testView2(TemplateView):
    template_name = 'develop/test.html'