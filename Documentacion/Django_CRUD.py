# 2. Instalación de aplicaciones y otros ajustes importantes
# Para instalar la aplicación, solo tiene que agregar el nombre de la aplicación en la lista de INSTALLED_APPS. Esto está dentro settings.py archivo.

# DataFlair Static Files Settings
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static-files')
#DataFlair #User_Uploaded_Files
MEDIA_URL = 'media/'
MEDIA_ROOT=os.path.join(BASE_DIR, 'media')

# 3. Hacer modelos para libros app
# En la carpeta del libro, abra models.py y pegue este código. Estamos haciendo un modelo o tabla de base de datos para nuestra aplicación de libros.

from django.db import models
#DataFlair Models
class Book(models.Model):
    name = models.CharField(max_length = 50)
    picture = models.ImageField()
    author = models.CharField(max_length = 30, default=’anonymous’)
    email = models.EmailField(blank = True)
    describe = models.TextField(default = ‘DataFlair Django tutorials’)
    def __str__(self):
        return self.name

# Comprensión del código:
# A partir del código anterior, Django creará una tabla en una base de datos denominada book. Esa tabla tendrá estos campos:
# Nombre, imagen, autor, correo electrónico y descripción del objeto book. Desde esta clase, podemos manipular fácilmente la mesa. 
# La parte importante aquí es el campo de la imagen. Se establece como ImageField.
# Este ImageField es la razón por la que instalamos almohadas en este entorno virtual. 
# Django de forma predeterminada utiliza almohada (pillow) para manejar imágenes en ImageField. Así que, esos fueron los modelos de nuestra aplicación de libros.

# 4. Hacer formularios de modelo en el directorio de libros
# Django hace que sea mucho más fácil hacer formularios para modelos. Sólo necesitamos usar nuestros modelos y podemos hacer formularios fácilmente.
# Realice una nueva forms.py de archivos en el directorio book. Pegue este código en esta forms.py.

# Código:

from django import forms
from .models import Book

#DataFlair
class BookCreate(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

# Comprensión del código:
# Esta es una forma de modelo simple que hicimos para el modelo de libro. Aquí importamos dos clases, a saber, formularios y Libro. El Libro es el modelo que acabamos de hacer.
# La clase BookCreate() es la clase de formulario que representa el formulario Model. En MetaClass, definimos qué modelo se utilizará para hacer el formulario de modelo.
# Los campos denotan los campos de formulario reales donde queremos la entrada del usuario. Esta forma es suficiente para nuestro trabajo.

# 5. Registro del modelo en Django Admin
# Aquí estamos editando admin.py existentes en la carpeta de libros. Importe el modelo que desea registrar en el administrador. En este caso, es un libro.
# A continuación, pegue esta línea debajo de ella.

admin.site.register(Book)

# ‎Bien, hemos hecho un montón de backend aquí. Para implementar todo esto, ejecute estos comandos en la línea de comandos:‎
python manage.py makemigrations
python manage.py migrate

# ‎6. Hacer funciones de vista para Django CRUD App‎
# ‎Las funciones de vista son nuestras operaciones CRUD reales en Django. Ahora, estamos editando‎‎ views.py‎‎ en la carpeta ‎‎del libro.‎
# ‎Abra‎‎ views.py‎‎ archivo en la carpeta. Pegue este código en él:‎

from django.shortcuts import render, redirect
from .models import Book
from .forms import BookCreate
from django.http import HttpResponse

#DataFlair

# 1. Index Function
# ‎Esta función está realizando la operación de lectura. En esta función, simplemente recuperamos todos los objetos de la tabla de libros. A continuación, esos objetos se pasan a la plantilla correspondiente.‎
# ‎Estamos usando Querysets aquí para ese propósito. Como se describe en artículos anteriores: los conjuntos de consultas se usan para recuperar datos de tablas. Hay todo tipo de filtros y el uso de Querysets y aquí estamos usando:‎
#                                       Book.objects.all()
# ‎De la consulta se desprende claramente que está pasando un conjunto de todos los objetos de la tabla de libros.‎

def index(request):
    shelf = Book.objects.all()
    return render(request, 'book/library.html', {'shelf': shelf})

# 2. Upload Function    
# ‎Esta función es ‎‎operación CREATE‎‎ de CRUD. Simplemente está tomando datos de formulario del usuario y guardándolos en una base de datos. Puesto que hicimos un formulario de modelo para eso, no necesitamos validar los datos de nuevo. Podemos guardar directamente la información del formulario en la base de datos.‎
# ‎Primero creamos el objeto de formulario. A continuación, comprobamos si el formulario envía datos o el usuario está visitando por primera vez.‎
# ‎Si el método de solicitud de formulario es POST, significa que se está presentando el formulario. Puede ver, también se comprueba si el formulario también tiene un archivo de imagen o no. ‎‎ FILES‎‎ es un objeto similar a un diccionario que contiene los ARCHIVOS y otra información.‎
# ‎A continuación, comprobamos si los datos introducidos por el usuario son correctos o no. Esto se hace mediante ‎‎form_object.is_clean()‎‎ método. Esto devolverá True o False si el form_object contiene datos válidos o no.‎
# ‎Si la respuesta es True, guardamos los datos del formulario recibidos en la base de datos. ‎‎form_object.save()‎‎ logra esto y como es un formulario de modelo, podemos usarlo directamente.‎
# ‎Si recibimos una solicitud GET, devolvemos un formulario vacío. Así es como podemos crear un objeto en la base de datos.‎

def upload(request):
    upload = BookCreate()
    if request.method == 'POST':
        upload = BookCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
else:
        return render(request, 'book/upload_form.html', {'upload_form':upload})


# 3. Update_book Function
# ‎La función de update_book es un poco similar a la función de actualización. Sin embargo, hace más que eso. La función update_book toma dos parámetros de la solicitud. La solicitud en sí y el número de identificación. El número de identificación se utiliza para identificar el objeto que se va a editar.‎
# ‎Puede pasarlo como una URL o como una cookie. El método de sesión es el más seguro, pero no necesitamos usarlo aquí. Por lo tanto, la función update_book comprobará si el book_id es válido o no.‎
# ‎Si el objeto existe, devolverá el formulario rellenado con la información del objeto en él. El usuario puede cambiar el formulario de nuevo. En este caso, no habrá creación de nuevo libro sino la edición del objeto de libro existente.‎

def update_book(request, book_id):
    book_id = int(book_id)
    try:
        book_sel = Book.objects.get(id = book_id)
    except Book.DoesNotExist:
        return redirect('index')
    book_form = BookCreate(request.POST or None, instance = book_sel)
    if book_form.is_valid():
       book_form.save()
       return redirect('index')
    return render(request, 'book/upload_form.html', {'upload_form':book_form})

# 4. Delete Function
# ‎Eliminar función es la última función de la aplicación CRUD. Volvemos a usar el mismo método de objeto que con la función Update book. Estamos pasando la solicitud y book_id para eliminar el libro.‎
# ‎Esta es una interpretación más simple de update_book función.‎
# ‎El queryset ‎‎book.objects.get(id = book_id)‎‎ comprobará si los libros tienen un identificador igual a book_id. Dado que book_id es una clave principal, solo se devolverá un objeto. Podemos eliminar ese objeto fácilmente simplemente ejecutando:‎
#                 ‎Método Book.delete().‎‎ 
# Esto eliminará el libro de la base de datos.‎
# ‎Por lo tanto, estas eran las funciones de vista. Ahora, estamos listos para hacer las plantillas y completar nuestra aplicación.‎

def delete_book(request, book_id):
    book_id = int(book_id)
    try:
        book_sel = Book.objects.get(id = book_id)
    except Book.DoesNotExist:
        return redirect('index')
    book_sel.delete()
    return redirect('index')

# 7. Making Templates
# The first thing you need to do is to make the templates folder in the book folder. Inside book/templates, make another folder book. We are going to make all our templates in that folder.
# Inside book/templates/book, make a new file:
# library.html

<!DOCTYPE html>
{% load static %}
<html>
<head>
    <title>Books App</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
</head>
<body style="background-color:#4DB6AC;">
<nav class="navbar navbar-light" style="background-color:#FF0033;">
    <a href="#" class="navbar-brand" style="background-color:#FFCC33;color:#000000;border-width:10px;border-color:#FFCC33;border-style:solid;border-spacing:30px;border-radius: 5px;">Library App</a>
    <a class="navbar-link btn-lg" href="{% url 'index' %}" style="background-color:#FFCC33;color:#000000;">DataFlair</a>
<a href="{% url 'admin:index' %}" class = 'navbar-link btn-lg' style="background-color:#FFCC33;color:#000000;">Admin</a>
    <a href="{% url 'upload-book' %}" class="navbar-link btn-lg" style="background-color:#FFCC33;color:#000000;">Upload Books</a>
</nav>
<br>
{% block content %}
<div class="card-columns">
    {% for book in shelf %}
    <div class="card" style="width: 18rem;">
  <img class="card-img-top" src="{{ book.picture.url }}">
  <div class="card-body">
    <h5 class="card-title">{{ book.name }}</h5>
    <p class="card-text">{{ book.describe }}</p>
   <div class="card-footer bg-transparent border-dark">
   <p class="card-title">{{book.author}}</p>
   <center>
       <a href="update/{{book.id}}" class="btn btn-warning" id = '{{book.id}}'>edit</a>
       <a href="delete/{{book.id}}" class="btn btn-danger" id = '{{book.id}}'>delete</a>
    </center>
    </div>
  </div>
</div>
    {% endfor %}
</div>
{% endblock %}
</body>
</html>

# ‎Comprensión del código:‎
# ‎Es un archivo de plantilla simple donde estamos mostrando objetos de una base de datos. Estamos ejecutando un bucle for para acceder a los datos del diccionario que pasamos. Todas las demás cosas son CSS y algún Marco Bootstrap.‎


# Upload_form.html
# Code:

{% extends 'book/library.html' %}
{% block content %}
    <center>
    <h1 class="display-3" style="background-color:#000000;color:#FFFF99;">Upload Books</h1>
    <form method = 'POST' enctype="multipart/form-data">
        {% csrf_token %}
        <table class = 'w-50 table table-light' style="border-radius:10px;background-color:#FFFF99;">
            {% for field in upload_form %}
            <tr>
                <th>{{field.label}}</th>
                <td>{{ field }}</td>
            </tr>
            {% endfor %}
        </table>
        <button type="submit" class="btn btn-lg btn-warning">Submit</button>
    </form>
</center>
{% endblock %}

# ‎Comprensión del código:‎

# ‎Esta es una plantilla de representación de formulario típica. Estamos usando csrf token y otras etiquetas de formulario. Aquí estoy imprimiendo los campos de formulario a través de bucle for. Esto se puede hacer de otra manera directamente. Depende de cómo desee representarlo en front-end.‎

# ‎8. Configuración de direcciones URL‎
# ‎Ahora, necesitamos configurar el archivo urls. Pegue este código tal como está en los archivos url mencionados. Si el archivo no existe, haga uno y copie todo.‎
# Urls.py


from django.contrib import admin
from django.urls import path, include
#DataFlair
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('book.urls'))
]

# Book/urls.py

from django.urls import path
from . import views
from libraryapp.settings import DEBUG, STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name = 'index'),
    path('upload/', views.upload, name = 'upload-book'),
    path('update/<int:book_id>', views.update_book),
    path('delete/<int:book_id>', views.delete_book)
]

#DataFlair
if DEBUG:
    urlpatterns += static(STATIC_URL, document_root = STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root = MEDIA_ROOT)
    
    
# ‎Este archivo contiene todas las búsquedas de URL para la aplicación de biblioteca, así como la configuración de archivos estáticos de Django. Django utiliza esta configuración para representar las imágenes con el objeto book.‎

# 9. Running Server and Testing
# At last, the fun part. To test the website, start your server by:

python manage.py runserver