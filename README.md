# Clase 7 - Blog CRUD con Django

Este proyecto es una aplicación web de blog desarrollada con Django. Permite crear, leer, actualizar y eliminar (CRUD) publicaciones de blog.

## Características

- Gestión de publicaciones (posts) con título, cuerpo, fechas y autor.
- Panel de administración de Django personalizado para visualizar y gestionar posts.
- Uso de base de datos SQLite por defecto.
- Estructura lista para desarrollo y pruebas locales.

## Requisitos

- Python 3.10+
- Django 5.2.6

## Instalación

1. Clona el repositorio:
   ```sh
   git clone <URL_DEL_REPOSITORIO>
   cd clase7_blog_crud
   ```

2. Crea un entorno virtual e instálalo:
   ```sh
   python -m venv venv
   venv\Scripts\activate
   pip install django
   ```

3. Aplica migraciones:
   ```sh
   python manage.py migrate
   ```

4. Crea un superusuario para acceder al admin:
   ```sh
   python manage.py createsuperuser
   ```

5. Ejecuta el servidor de desarrollo:
   ```sh
   python manage.py runserver
   ```

6. Accede al panel de administración en [http://localhost:8000/admin/](http://localhost:8000/admin/)

## Estructura del Proyecto

```
clase7_blog_crud/
├── blogs/
│   ├── admin.py
│   ├── models.py
│   └── ...
├── django_base/
│   ├── settings.py
│   └──# Clase 7 - Blog CRUD con Django

Este proyecto es una aplicación web de blog desarrollada con Django. Permite crear, leer, actualizar y eliminar (CRUD) publicaciones de blog.

## Características

- Gestión de publicaciones (posts) con título, cuerpo, fechas y autor.
- Panel de administración de Django personalizado para visualizar y gestionar posts.
- Uso de base de datos SQLite por defecto.
- Estructura lista para desarrollo y pruebas locales.

## Requisitos

- Python 3.10+
- Django 5.2.6

## Instalación

1. Clona el repositorio:
   ```sh
   git clone <URL_DEL_REPOSITORIO>
   cd clase7_blog_crud
   ```

2. Crea un entorno virtual e instálalo:
   ```sh
   python -m venv venv
   venv\Scripts\activate
   pip install django
   ```

3. Aplica migraciones:
   ```sh
   python manage.py migrate
   ```

4. Crea un superusuario para acceder al admin:
   ```sh
   python manage.py createsuperuser
   ```

5. Ejecuta el servidor de desarrollo:
   ```sh
   python manage.py runserver
   ```

6. Accede al panel de administración en [http://localhost:8000/admin/](http://localhost:8000/admin/)

## Estructura del Proyecto

```
clase7_blog_crud/
├── blogs/
│   ├── admin.py
│   ├── models.py
│   └── ...
├── django_base/
│   ├── settings.py
│   └──