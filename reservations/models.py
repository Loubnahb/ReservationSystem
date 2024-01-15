from django.db import models
from django.conf import settings
from salle.models import Salle  # Import the Salle model

class Reservation(models.Model):
    salle = models.ForeignKey('salle.Salle', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200, verbose_name="Titre réunion")
    date = models.DateField(verbose_name="Date réunion")
    start_time = models.TimeField(verbose_name="Heure de début")
    end_time = models.TimeField(verbose_name="Heure de fin")
    description = models.TextField(verbose_name="Description de la réunion")
    attendees = models.ManyToManyField(settings.AUTH_USER_MODEL, verbose_name="Inviter employés")
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='created_reservations', verbose_name="Créateur de la réservation",null=True,)


    def __str__(self):
        return self.title
