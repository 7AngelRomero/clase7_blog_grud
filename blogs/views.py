from django.shortcuts import render

# Create your views here.
from .models import Post  # Importa el modelo Post desde models.py

def post_list(request):
    posts = Post.objects.all().order_by('created_at') # Obtiene todos los posts ordenados por fecha de creación
    return render(request, 'post_list.html', {'posts': posts})  # Renderiza la plantilla post_list.html con los posts