from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Usuarios)
admin.site.site_header = "Sistema de Gestión de Usuarios"
admin.site.site_title = "Sistema de Gestión de Usuarios"
admin.site.index_title = "Bienvenido al sistema de gestión de usuarios"