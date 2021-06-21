"""SystemConfig URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import Settings, settings
from django.conf.urls.static import static

from Apps.HomePage.views import IndexView
from Apps.AppLogin.views import *
from Apps.AppMain.views import abrirIndex
from Apps.AppSistemas.views.test.views import testView2

urlpatterns = [
    path('', IndexView.as_view()),
    path('login/', include('Apps.AppLogin.urls')),
    path('admin/', admin.site.urls),
    path('sis/', include('Apps.AppSistemas.urls')),
    
    
    path('Horus/', abrirIndex, name='index'),
    path('dashboard/', include('Apps.AppDashboard.urls')),
    path('test/', testView2.as_view(), name='openTestHTML'),
    # path('Horus/sistemas/', include('Apps.AppSistemas.urls')),
    # path('Horus/admininstracion/', include('Apps.AppAdministracion.urls')),
]
# Para trabajar con archivos MEDIA
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)