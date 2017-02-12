from django.contrib import admin
from .models import AuditType, AuditSections

@admin.register(AuditType)
class AuditTypeAdmin(admin.ModelAdmin):
    list_display = ('type_title', 'audit_type_fld', 'audit_regulation')

@admin.register(AuditSections)
class AuditSectionsAdmin(admin.ModelAdmin):
    search_fields = ['audit_type', 'section_number', 'section_heading']
    list_display = ('audit_type', 'section_number', 'section_heading')
    list_filter = ['audit_type', 'section_heading']
