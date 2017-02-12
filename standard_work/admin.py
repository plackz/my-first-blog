from django.contrib import admin
from .models import StandardWork, WorkGuidance, WorkRemarks

# define the admin class
@admin.register(StandardWork)
class StandardWorkAdmin(admin.ModelAdmin):
    date_hierarchy = 'work_last_dt'
    search_fields = ['work_title', 'work_frequency', 'work_last_dt']
    list_display = ('work_title', 'work_frequency', 'work_last_dt', 'work_next_dt')
    list_filter = ['work_frequency','work_next_dt']

@admin.register(WorkGuidance)
class WorkGuidanceAdmin(admin.ModelAdmin):
    search_fields = ['guide_title', 'guide_text']
    list_display = ('guide_title', 'guide_text')

@admin.register(WorkRemarks)
class WorkRemarks(admin.ModelAdmin):
    serach_fields = ['remark_title', 'remark_guide', 'remark_text', 'remark_created']
    list_display = ('remark_title', 'remark_guide', 'remark_text', 'remark_created')
    list_filter = ['remark_title','remark_guide', 'remark_created']
