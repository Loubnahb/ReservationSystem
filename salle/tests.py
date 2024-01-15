from django.test import TestCase
from .models import Salle, Equipement

class SalleModelTest(TestCase):

    def setUp(self):
        Equipement.objects.create(nom="Projecteur")

    def test_salle_creation(self):
        equipement = Equipement.objects.get(nom="Projecteur")
        salle = Salle.objects.create(
            nom='Salle A',
            adresse='123 Test Street',
            batiment_etage='Building 1, Floor 2',
            capacite=10
        )
        salle.equipements.add(equipement)

        self.assertEqual(salle.nom, 'Salle A')
        self.assertIn(equipement, salle.equipements.all())

