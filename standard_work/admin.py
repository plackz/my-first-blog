from django.contrib import admin
from .models import StandardWork

# define the admin class
@admin.register(StandardWork)
class StandardWorkAdmin(admin.ModelAdmin):
    date_hierarchy = 'work_last_dt'
    search_fields = ['work_title', 'work_frequency', 'work_last_dt']
    list_display = ('work_title', 'work_frequency', 'work_last_dt', 'work_next_dt')
    list_filter = ['work_frequency','work_next_dt']
