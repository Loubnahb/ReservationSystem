# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ReservationForm
from .models import Reservation
from django.contrib.auth.decorators import login_required
from salle.models import Salle
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from employe.models import Employe
from django.utils import timezone
from django.contrib.admin.views.decorators import staff_member_required



@login_required
def create_reservation(request, salle_id):
    """
    Permet à l'utilisateur de créer une nouvelle réservation pour une salle spécifique.
    Affiche un formulaire de réservation et traite les données soumises.
    Redirige vers la liste des réservations après une création réussie.
    """
    salle = get_object_or_404(Salle, pk=salle_id)
    if request.method == 'POST':
        form = ReservationForm(request.POST, user=request.user)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.creator = request.user
            reservation.salle = salle
            reservation.save()
            # If you have a ManyToMany field that needs to be saved, call save_m2m()
            form.save_m2m()
            return redirect('reservations:reservations_list')
    else:
        # When the form is first presented to the user, exclude the user from the list of attendees
        form = ReservationForm(user=request.user, initial={'salle': salle})
    return render(request, 'reservations/reservation_form.html', {'form': form, 'salle': salle})

def reservations_list(request):
    """
    Affiche la liste de toutes les réservations créées par l'utilisateur actuel.
    Trie les réservations par date et heure de début.
    """
    reservations = Reservation.objects.filter(creator=request.user).order_by('-date', 'start_time')
    return render(request, 'reservations/reservations_list.html', {'reservations': reservations})

@login_required
@user_passes_test(lambda u: u.is_staff)  # Only allow staff members to access this view
def admin_reservations_list(request):
    """
    Vue réservée aux administrateurs pour afficher toutes les réservations existantes.
    Trie les réservations par date et heure de début.
    """    
# Get all reservations without filtering by the creator
    reservations = Reservation.objects.all().order_by('-date', 'start_time')
# Pass the reservations to the template
    return render(request, 'reservations/admin_reservations_list.html', {'reservations': reservations})

@login_required
@user_passes_test(lambda u: u.is_staff)
def change_reservation(request, reservation_id):
    """
    Permet aux administrateurs de modifier une réservation existante.
    Affiche un formulaire prérempli et enregistre les modifications.
    """
    reservation = get_object_or_404(Reservation, pk=reservation_id)
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return redirect('reservations:admin_reservations_list')
    else:
        form = ReservationForm(instance=reservation)
    context = {
        'form': form,
        'salle': reservation.salle,
        'reservation': reservation,  # Make sure this line is present
    }
    return render(request, 'reservations/reservation_form.html', context)


@login_required
@user_passes_test(lambda u: u.is_staff)
def delete_reservation(request, reservation_id):
    """
    Permet aux administrateurs de supprimer une réservation existante.
    Demande une confirmation avant la suppression définitive.
    """
    reservation = get_object_or_404(Reservation, pk=reservation_id)
    if request.method == 'POST':
        reservation.delete()
        return redirect('reservations:admin_reservations_list')
    return render(request, 'reservations/reservation_confirm_delete.html', {'reservation': reservation})


@login_required
def modify_reservation(request, reservation_id):
    """
    Permet à l'utilisateur qui a créé une réservation de la modifier.
    Affiche un formulaire prérempli et enregistre les modifications.
    """
    reservation = get_object_or_404(Reservation, pk=reservation_id, creator=request.user)
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Reservation updated successfully.")
            return redirect('reservations:reservations_list')
    else:
        form = ReservationForm(instance=reservation, user=request.user)
    return render(request, 'reservations/reservation_form.html', {'form': form, 'salle': reservation.salle})

@login_required
def cancel_reservation(request, reservation_id):
    """
    Permet à l'utilisateur qui a créé une réservation de l'annuler.
    Demande une confirmation avant l'annulation définitive.
    """
    reservation = get_object_or_404(Reservation, pk=reservation_id, creator=request.user)
    if request.method == 'POST':
        reservation.delete()
        return redirect('reservations:reservations_list')
    return render(request, 'reservations/reservation_confirm_cancel.html', {'reservation': reservation})

@staff_member_required
def custom_admin_dashboard_view(request):
    """
    Affiche un tableau de bord personnalisé pour les administrateurs.
    Inclut des statistiques comme le nombre d'employés, de salles, et de réservations à venir.
    """
    employee_count = Employe.objects.count()
    room_count = Salle.objects.count()
    reserved_room_count = Reservation.objects.filter(date__gte=timezone.now()).count()
    upcoming_meetings = Reservation.objects.filter(date__gte=timezone.now()).order_by('date', 'start_time')[:5]

    print("Employee count:", employee_count)
    print("Room count:", room_count)
    print("Reserved room count:", reserved_room_count)

    context = {
        'employee_count': employee_count,
        'room_count': room_count,
        'reserved_room_count': reserved_room_count,
        'upcoming_meetings': upcoming_meetings,
    }
    
    
    
    return render(request, 'admin/base_site.html', context)

from django.db.models import Q

def user_dashboard_view(request):
    """
    Display a personalized dashboard for the logged-in user (employee).
    Includes statistics like the total number of meetings, completed meetings, and today's meetings for that user.
    """
    # Count the total number of meetings for the logged-in user
    total_meetings_count = Reservation.objects.filter(creator=request.user).count()

    # Determine the current time to compare with meeting end times
    current_datetime = timezone.localtime()

    # Count the total number of completed meetings for the logged-in user
    # A meeting is considered completed if its end time is in the past
    completed_meetings_queryset = Reservation.objects.filter(
        Q(creator=request.user, date__lt=current_datetime.date()) |
        Q(creator=request.user, date=current_datetime.date(), end_time__lt=current_datetime.time())
    )
    completed_meetings_count = completed_meetings_queryset.count()

    # Count the number of today's meetings for the logged-in user
    todays_meetings_count = Reservation.objects.filter(
        creator=request.user,
        date=current_datetime.date()
    ).count()

    context = {
        'total_meetings_count': total_meetings_count,
        'completed_meetings_count': completed_meetings_count,
        'todays_meetings_count': todays_meetings_count,
    }

    return render(request, 'user/user_home.html', context)
