# blog/views.py

from django.shortcuts import render
# Importa tu modelo Post
from .models import Post
# Importa la función timezone para filtrar por fecha de publicación
from django.utils import timezone 

def post_list(request):
    # Obtiene todos los posts publicados y los ordena por fecha de publicación descendente
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    
    # Envía la lista de posts al template usando un diccionario (contexto)
    return render(request, 'blog/post_list.html', {'posts': posts})