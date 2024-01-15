from django.test import TestCase
from .models import Employe
from django.utils import timezone

class EmployeModelTest(TestCase):

    def test_employe_creation(self):
        employe = Employe.objects.create_user(
            username='testuser', 
            email='test@example.com', 
            password='testpassword',
            numero_de_telephone='123456789',
            fonction='Developer',
            departement='IT',
            adresse='123 Test Street',
            date_de_naissance=timezone.now().date(),
            date_dentree=timezone.now().date()
        )
        self.assertEqual(employe.username, 'testuser')
        self.assertEqual(employe.email, 'test@example.com')
        self.assertEqual(employe.fonction, 'Developer')
        self.assertIsNotNone(employe.date_de_naissance)

