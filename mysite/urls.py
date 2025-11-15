"""
URL configuration for mysite project.
...
"""
from django.contrib import admin
from django.urls import path, include  # <-- ¡Paso 1: Importar 'include'!

urlpatterns = [
    # Ruta para el panel de administración
    path('admin/', admin.site.urls),
    
    # ¡Paso 2: Agregar la ruta del blog!
    # Esto le dice a Django: si la URL está vacía (''), busca el resto de las URLs en 'blog.urls'
    path('', include('blog.urls')), 
]
