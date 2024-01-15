from django import template
from django.urls import reverse

register = template.Library()

@register.inclusion_tag('admin/sidebar.html')
def admin_sidebar():
    employe_change_url = reverse('admin:employe_employe_changelist')
    return {'employe_change_url': employe_change_url}
