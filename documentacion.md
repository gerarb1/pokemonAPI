## 🛠️ Tecnologías utilizadas
- Django
- Django REST Framework
- Django Extensions
- Pydot

## Pasos que seguí en el desarrollo

1. **Diseño del modelo entidad-relación**:
   - Analicé qué entidades necesitaba (Pokémon, Tipos, Habilidades, Evoluciones, etc.).


2. **Entorno de desarrollo**:
   - Creé un entorno virtual con `venv`.
   - Instalé las dependencias necesarias: `djangorestframework`, `django-extensions`, `pydot`.

3. **Creación del proyecto Django**:
```bash
   django-admin startproject api_pokemon
   cd api_pokemon
   python manage.py startapp pokemon
```
4. **crear los modelos**
```python 
    from django.db import models
class Tipo(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()

class Habilidad(models.Model):
    nombre = models.CharField(max_length=50)
    efecto = models.TextField()

class Movimiento(models.Model):
    nombre = models.CharField(max_length=50)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    poder = models.IntegerField()
    precision = models.IntegerField()

class Pokemon(models.Model):
    nombre = models.CharField(max_length=100)
    tipos = models.ManyToManyField(Tipo)
    habilidades = models.ManyToManyField(Habilidad)
    movimientos = models.ManyToManyField(Movimiento)
    evolucion = models.OneToOneField('self', null=True, blank=True, on_delete=models.SET_NULL)

    hacer las migraciones
    python manage.py makemigrations
    python manage.py migrate
```
5. **hacer las migraciones**
```bash
python manage.py makemigrations
python manage.py migrate
```
6. **graficas los modelos**
``` bash
python manage.py graph_models pokemon -o pokemon_models.png
```
## 🗺️ Diagrama entidad-relación

Este es el modelo entidad-relación usado en el proyecto:

![Modelo ER](modelo.png)

## Enpoints disponibles
| Método | Endpoint             | Descripción                        |
|--------|----------------------|------------------------------------|
| GET    | /api/pokemon/        | Lista todos los Pokémon            |
| POST   | /api/pokemon/        | Crea un nuevo Pokémon              |
| GET    | /api/pokemon/{id}/   | Detalle de un Pokémon              |
| GET    | /api/tipo/           | Lista todos los tipos              |
| GET    | /api/habilidades/    | Lista todas las habilidades        |
| GET    | /api/movimientos/    | Lista todos los movimientos        |


