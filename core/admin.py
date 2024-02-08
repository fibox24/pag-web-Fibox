from django.contrib import admin
from .models import Plan
# Register your models here.
class PlanesAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'precio')
    search_fields = ('nombre', 'descripcion', 'precio')
    list_filter = ('nombre', 'descripcion', 'precio')
    readonly_fields = ('created', 'updated')

admin.site.register(Plan, PlanesAdmin)