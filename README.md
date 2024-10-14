# django-auth-crud
Este repositorio contiene una práctica de [Django](https://www.djangoproject.com/) basada en el siguiente video de YouTube:
[Django CRUD con Autenticacion y Despliegue Gratuito (Login,Register, Rutas protegidas, y mas)](https://www.youtube.com/watch?v=e6PkGDH4wWA)

## Descripción
La aplicación es un **seguidor de tareas** simple que permite gestionar tareas de múltiples usuarios mediante funcionalidades de CRUD (Create, Read, Update, Delete). La autenticación permite que cada usuario maneje sus propias tareas en un entorno seguro.
- `Frontend:` Los pocos estilos fueron implementados usando [Bootstrap](https://getbootstrap.com/).
- `Backend:` La persistencia de datos se maneja con **PostgreSQL**.
- `Hosting:` La aplicación está alojada de forma gratuita en [Render](https://render.com/).

## Funcionalidades
- Registro e inicio de sesión de usuarios.
- Creación, visualización, actualización y eliminación de tareas.
- Rutas protegidas que requieren autenticación.
- Gestión separada de tareas por usuario.

## Deployment
[Accede a la app aquí](https://django-auth-crud-3b6x.onrender.com).

## Instrucciones para correr el proyecto localmente
1. Clona el repositorio:
```bash
git clone git@github.com:luismarrer/django-auth-crud.git
cd django-auth-crud
```
2. Configura el entorno virtual:
```bash
python -m venv venv
source venv/bin/activate  # En Linux/macOS
venv\Scripts\activate  # En Windows
```
3. Instala las dependencias:
```bash
pip install -r requirements.txt
```
4. Aplica las migraciones:
```bash
python manage.py migrate
```
5. Inicia el servidor:
```bash
python manage.py runserver
```
6. Accede a la aplicación desde tu navegador en http://localhost:8000.
