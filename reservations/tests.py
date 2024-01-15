from django.test import TestCase
from .models import Reservation, Salle
from employe.models import Employe

class ReservationModelTest(TestCase):

    def setUp(self):
        self.employe = Employe.objects.create_user(username='testuser', password='12345')
        self.salle = Salle.objects.create(nom='Test Salle', capacite=10)

    def test_reservation_creation(self):
        reservation = Reservation.objects.create(
            salle=self.salle,
            title='Test Meeting',
            date='2024-01-01',
            start_time='09:00',
            end_time='10:00',
            creator=self.employe
        )
        reservation.attendees.add(self.employe)

        self.assertEqual(reservation.title, 'Test Meeting')
        self.assertEqual(reservation.creator, self.employe)
        self.assertIn(self.employe, reservation.attendees.all())
