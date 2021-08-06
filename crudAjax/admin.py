from django.contrib import admin
from .models import Usuario

# Register your models here.
@admin.register(Usuario)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','nombre','email','password','telefono','fecha_nacimiento')