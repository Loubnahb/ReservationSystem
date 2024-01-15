from django.contrib.auth.models import AbstractUser
from django.db import models

class Employe(AbstractUser):
    numero_de_telephone = models.CharField(max_length=15, verbose_name='Numéro de téléphone', null=True, blank=True)
    fonction = models.CharField(max_length=100, verbose_name='Fonction', null=True, blank=True)
    departement = models.CharField(max_length=100, verbose_name='Département', null=True, blank=True)
    adresse = models.CharField(max_length=255, verbose_name='Adresse', null=True, blank=True)
    date_de_naissance = models.DateField(verbose_name='Date de naissance', null=True, blank=True)
    date_dentree = models.DateField(verbose_name='Date d\'entrée', null=True, blank=True)
