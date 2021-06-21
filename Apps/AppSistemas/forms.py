from datetime import datetime

from django.forms import *

from Apps.AppSistemas.models import *

# Creo un formulario con los campos del Modelo
class CategoryForm(ModelForm):
    # Cuando hay atributos que se repiten (estan en todos los campos), se sobreescribe el método __init__ del formulario, que inicializa los campos.
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Si utilizamos widget_tweaks, comentamos el siguiente for, y se modifica en el template:
        # for form in self.visible_fields():
        #     form.field.widget.attrs['class'] = 'form-control'
        #     form.field.widget.attrs['autocomplete'] = 'off'
                
    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'name': TextInput(
                attrs={
                    'placeholder': 'Ingrese un nombre',
                }
            ),
            'desc': Textarea(
                attrs={
                    'placeholder': 'Ingrese un nombre',
                    'rows': 3,
                    'cols': 3
                }
            ),
        }
    
    # Sobreescribimos el método save() del form para enviar los datos por ajax
    def save(self, *args, **kwargs):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data
    
    # Sobreescibir el método que contiene los errores del formulario
    def clean(self):
        cleaned = super().clean() # Devuelve un diccionario {'campo':'valor', ...}
        # Podemos agregarle validaciones a los campos del formulario enviado
        # if len(cleaned['name']) <= 50:
        #     self.add_error('name', 'Le faltan carácteres')
        # print(cleaned)
        return cleaned

class ProductForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['autofocus'] = True

    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'name': TextInput(
                attrs={
                    'placeholder': 'Ingrese un nombre',
                }
            ),
            'cat': Select(
                attrs={
                    'class': 'select2',
                    'style': 'width: 100%'
                }
            ),
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

class ClientForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['names'].widget.attrs['autofocus'] = True

    class Meta:
        model = Client
        fields = '__all__'
        widgets = {
            'names': TextInput(
                attrs={
                    'placeholder': 'Ingrese sus nombres',
                }
            ),
            'surnames': TextInput(
                attrs={
                    'placeholder': 'Ingrese sus apellidos',
                }
            ),
            'dni': TextInput(
                attrs={
                    'placeholder': 'Ingrese su dni',
                }
            ),
            'date_birthday': DateInput(format='%Y-%m-%d',
                                       attrs={
                                           'value': datetime.now().strftime('%Y-%m-%d'),
                                       }
                                       ),
            'address': TextInput(
                attrs={
                    'placeholder': 'Ingrese su dirección',
                }
            ),
            'gender': Select()
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

class TestForm(Form):
    # Formulario que contendrá los selects
    # Configuro mi formulario con un campo select que tendrá el listado de todas las categorías
    categories = ModelChoiceField(queryset=Category.objects.all(), widget=Select(attrs={
        'class':'form-control select2',
        'style': 'width: 100%'
    }))
    
    # Cuando seleccionemos un valor en 'categories', nos tiene que mostrar todos los productos que tengan la categoría seleccionada
    # Creamos otro componente.
    products = ModelChoiceField(queryset=Product.objects.none(), widget=Select(attrs={
        'class':'form-control select2',
        'style': 'width: 100%'
    }))
    
    search = CharField(widget=TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Ingrese una descripcion'
    }))
    
# Creo un formulario con los campos del Modelo
class ZonasForm(ModelForm):
    # Cuando hay atributos que se repiten (estan en todos los campos), se sobreescribe el método __init__ del formulario, que inicializa los campos.
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Si utilizamos widget_tweaks, comentamos el siguiente for, y se modifica en el template:
        # for form in self.visible_fields():
        #     form.field.widget.attrs['class'] = 'form-control'
        #     form.field.widget.attrs['autocomplete'] = 'off'
                
    class Meta:
        model = Zonas
        fields = '__all__' # Selecciono los campos a mostrar en el formulario, ej.: ['pub_date', 'headline', 'content', 'reporter']
        labels = {
            'descripcion':'Descripcion'
        }
        #Personalizar classes en los componentes del formulario
        widgets = {
            'descripcion': TextInput(
                attrs={
                    'placeholder':'Ingrese una categoría',
                }
            ),
            'campo1': Textarea(
                attrs={
                    'placeholder':'Ingrese una descripción',
                    'cols': 3,
                    'rows': 3
                }                
            )
        }
    
    # Sobreescribimos el método save() del form para enviar los datos por ajax
    def save(self, *args, **kwargs):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data
    
    # Sobreescibir el método que contiene los errores del formulario
    def clean(self):
        cleaned = super().clean() # Devuelve un diccionario {'campo':'valor', ...}
        # Podemos agregarle validaciones a los campos del formulario enviado
        # if len(cleaned['name']) <= 50:
        #     self.add_error('name', 'Le faltan carácteres')
        # print(cleaned)
        return cleaned

# Formulario para la maquetación de la factura
class SaleForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Sale
        fields = '__all__'
        widgets = {
            'cli': Select(attrs={
                'class': 'form-control select2',
                'style': 'width: 100%'
            }),
            'date_joined': DateInput(
                format='%Y-%m-%d',
                attrs={
                    'value': datetime.now().strftime('%Y-%m-%d'),
                    'autocomplete': 'off',
                    'class': 'form-control datetimepicker-input',
                    'id': 'date_joined',
                    'data-target': '#date_joined',
                    'data-toggle': 'datetimepicker'
                }
            ),
            'iva': TextInput(attrs={
                'class': 'form-control',
            }),
            'subtotal': TextInput(attrs={
                'readonly': True,
                'class': 'form-control',
            }),
            'total': TextInput(attrs={
                'readonly': True,
                'class': 'form-control',
            })
        }

class ProductFormSet(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Product
        fields = '__all__'