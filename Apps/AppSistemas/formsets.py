from django.forms import formset_factory
from django.urls import reverse_lazy
from django.views.generic.edit import FormView

from Apps.AppSistemas.models import Product
from Apps.AppSistemas.forms import ProductForm, ProductFormSet

class FormsetProduct(FormView):
    template_name = 'product/prod_formset.html'
    form_class = formset_factory(ProductFormSet, extra=3)
    success_url = reverse_lazy('index')
    
    def form_valid(self, form):
        for f in form:
            if f.is_valid():
                f.save()
        return super().form_valid(form)