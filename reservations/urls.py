from django.urls import path
from .views import (
    create_reservation,
    reservations_list,
    admin_reservations_list,
    change_reservation,
    delete_reservation,
    modify_reservation,
    cancel_reservation,
)


app_name = 'reservations'

urlpatterns = [
    path('create/<int:salle_id>/', create_reservation, name='create_reservation'),
    path('list/', reservations_list, name='reservations_list'),
    
    path('dashboard/', admin_reservations_list, name='admin_reservations_list'),
    path('dashboard/change/<int:reservation_id>/', change_reservation, name='reservation_change'),
    path('dashboard/delete/<int:reservation_id>/', delete_reservation, name='reservation_delete'),
    path('modify/<int:reservation_id>/', modify_reservation, name='modify_reservation'),
    path('cancel/<int:reservation_id>/', cancel_reservation, name='cancel_reservation'),
    # Add other reservations-specific URLs here if needed
]