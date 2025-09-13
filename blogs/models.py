from django.db import models

# Create your models here :).

# Se va a crear una tabla que contenga los siguientes atributos: titulo, cuerpo, fecha de publicacion, autor

class Post(models.Model):
    title = models.CharField(max_length=200)  # Titulo del post, maximo 200 caracteres
    body = models.TextField()  # Cuerpo del post, campo de texto largo
    created_at = models.DateTimeField(auto_now_add=True)  # Fecha de creación, se asigna automaticamente al crear
    updated_at = models.DateTimeField(auto_now=True)  # Fecha de actualización, se asigna automaticamente al actualizar
    author = models.ForeignKey(
                            "auth.User",  # Relacion con el modelo User de Django
                            on_delete=models.CASCADE  # Si el usuario se elimina, se eliminan sus posts
                            )
    
    def __str__(self):
        return self.title  # Representación en cadena del post, se muestra el titulo
