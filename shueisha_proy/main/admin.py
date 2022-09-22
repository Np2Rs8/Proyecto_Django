"""
    Importacion de librerias necesarias.

    Se importan las tablas de review, portada y blog.
"""
from django.contrib import admin
from . models import (
    Portada,
    Blog,
    Review,
    )


"""
    Se añaden a la vista de admin las diferentes tablas con los campos
    que se desean ver desde la interfaz.
"""
@admin.register(Portada)
class PortadaAdmin(admin.ModelAdmin):
    list_display = ('id','name','is_active')

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id','name','is_active')
    readonly_fields = ('slug',)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id','name','is_active')
    readonly_fields = ('slug',)
