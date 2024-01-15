from django.shortcuts import render
from .models import Salle

def salle_list(request):
    """
    Affiche la liste des salles disponibles, en excluant celles en maintenance.
    """
    salles = Salle.objects.exclude(etat='maintenance')
    return render(request, 'user/salle_list.html', {'salles': salles})
