from django.contrib import admin
from .models import Incidents

@admin.register(Incidents)
class IncidentsAdmin(admin.ModelAdmin):
    search_fields = ['incident_title', 'incident_text', 'incident_contact', 'root_cause', 'steps_to_fix']
    list_display = ('incident_title', 'incident_text', 'customer_affected','incident_contact', 'incident_dt', 'resolution_dt', 'resolved_time', 'root_cause', 'steps_to_fix', 'created_date')
    list_filter = ['incident_dt', 'resolution_dt']
