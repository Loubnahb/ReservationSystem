from django.contrib import admin
from .models import Salle, Equipement

@admin.register(Equipement)
class EquipementAdmin(admin.ModelAdmin):
    list_display = ('nom',)

@admin.register(Salle)
class SalleAdmin(admin.ModelAdmin):
    list_display = ('nom',)

