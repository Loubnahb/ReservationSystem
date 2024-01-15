"""
URL configuration for ReservationSystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.contrib.auth import views as auth_views
from reservations.views import custom_admin_dashboard_view
from django.contrib.admin.views.decorators import staff_member_required
from . import views  # Import views from the current directory if there are any project-level views
from .views import CustomLoginView  # Import from project-level views
from reservations.views import user_dashboard_view    

admin.site.index_template = 'admin/index.html'  # Pointing to your custom admin template

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('admin/', admin.site.urls),
    path('employe/', include('employe.urls', namespace='employe')),  # Including employe app urls
    path('reservations/', include('reservations.urls', namespace='reservations')),  # Including reservations app urls
    path('salles/', include('salle.urls', namespace='salle')),  # Including salle app urls
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),  # Global logout URL
    path('home/', user_dashboard_view, name='home'),  # Global home URL, assuming it's a project-level view
    re_path(r'^$', RedirectView.as_view(url='/home/'), name='root-redirect'),  # Redirect root to /home/
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)