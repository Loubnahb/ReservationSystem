from django.contrib import admin
from .models import Reservation


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'start_time', 'end_time', 'creator')
    list_filter = ('date', 'creator')
    search_fields = ('title', 'description', 'attendees__username')
    raw_id_fields = ('attendees',)  # Use if you have many users and a dropdown becomes impractical
    date_hierarchy = 'date'  # Enables navigation through dates
    ordering = ('date', 'start_time')
    fieldsets = (
        (None, {
            'fields': ('salle', 'title', 'date', 'start_time', 'end_time')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('description', 'attendees', 'creator'),
        }),
    )

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "creator":
            kwargs["initial"] = request.user.id
            return db_field.formfield(**kwargs)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def save_model(self, request, obj, form, change):
        if not obj.creator_id:
            obj.creator = request.user
        super().save_model(request, obj, form, change)




