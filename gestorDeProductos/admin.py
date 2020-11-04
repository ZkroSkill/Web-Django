from django.contrib import admin
from .models import producto, usuario
# Register your models here.
class AdminProductos(admin.ModelAdmin):
    list_display1 = ['codigo', 'descripcion', 'stock']
    list_filter1 = ['descripcion']
    search_fields1 = ['codigo', 'descripcion']
    list_display_links1 = ['descripcion']
admin.site.register(producto,AdminProductos)

class AdminUsuario(admin.ModelAdmin):
    list_display = ['rut', 'nombreC', 'email']
    list_filter = ['rut']
    search_fields = ['rut', 'nombreC']
    list_display_links = ['nombreC']

admin.site.register(usuario, AdminProductos)
