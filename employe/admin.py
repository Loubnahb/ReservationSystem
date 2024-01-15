from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import Employe
from django.contrib.auth.models import Group




class EmployeAdmin(UserAdmin):
    model = Employe
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'numero_de_telephone', 
                                         'fonction', 'departement', 'adresse', 'date_de_naissance', 'date_dentree')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'numero_de_telephone', 
                                         'fonction', 'departement', 'adresse', 'date_de_naissance', 'date_dentree')}),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'numero_de_telephone', 'fonction', 'departement')
    search_fields = ('username', 'first_name', 'last_name', 'email', 'fonction', 'departement')
    ordering = ('username',)

# Register your models here
admin.site.register(Employe, EmployeAdmin)
admin.site.unregister(Group)



