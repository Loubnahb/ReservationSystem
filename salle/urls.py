from django.urls import path
from .views import salle_list

app_name = 'salle'

urlpatterns = [
    path('list/', salle_list, name='salle_list'),
    # Add other salle-specific URLs here if needed
]