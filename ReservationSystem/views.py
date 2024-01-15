from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.shortcuts import redirect

class CustomLoginView(LoginView):
    """
    Vue de connexion personnalisée.
    """
    
    template_name = 'user/login.html'  # Modèle de connexion

    def get_success_url(self):
        """
        Redirige l'utilisateur après la connexion.
        Admins vers le dashboard admin, les autres vers la page d'accueil.
        """
        user = self.request.user
        if user.is_superuser:
            return reverse_lazy('admin:index')  # Dashboard admin
        else:
            return reverse_lazy('home')  # Page d'accueil utilisateur
        
@login_required
def user_home(request):
    return render(request, 'user/user_home.html')