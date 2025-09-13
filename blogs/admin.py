from django.contrib import admin
from .models import Post  # Importa el modelo Post desde models.py


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at', 'author')
    search_fields = ('title', 'body', 'author__username')  # Permite buscar por título, cuerpo y autor
    list_filter = ('created_at', 'author')  # Permite filtrar por fecha de creación y autor
    ordering = ('-created_at',)  # Ordena por fecha de creación de forma descendente


admin.site.register(Post, PostAdmin)  # Registra el modelo Post en el admin de Django

