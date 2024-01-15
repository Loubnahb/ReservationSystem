from django.db import models
from django.utils.translation import gettext_lazy as _

class Equipement(models.Model):
    nom = models.CharField(max_length=100, verbose_name=_("Nom de l'équipement"))

    def __str__(self):
        return self.nom

class Salle(models.Model):
    nom = models.CharField(max_length=100, verbose_name=_("Nom de la salle"))
    adresse = models.CharField(max_length=255, verbose_name=_("Adresse"))
    batiment_etage = models.CharField(max_length=100, verbose_name=_("Bâtiment/Étage"))
    etat = models.CharField(
        max_length=100,
        choices=(('disponible', _("Disponible")), ('maintenance', _("En maintenance"))),
        default='disponible',
        verbose_name=_("État")
    )
    capacite = models.IntegerField(verbose_name=_("Capacité"))
    equipements = models.ManyToManyField(Equipement, verbose_name=_("Équipements"))
    image = models.ImageField(upload_to='salles_images/', verbose_name=_("Image"), null=True, blank=True)
    description = models.TextField(verbose_name=_("Description"), null=True, blank=True)

    def __str__(self):
        return self.nom

