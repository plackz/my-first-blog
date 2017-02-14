from django.contrib import admin
from .models import AuditType, AuditSections, AuditQuestions

@admin.register(AuditType)
class AuditTypeAdmin(admin.ModelAdmin):
    list_display = ('type_title', 'audit_type_fld', 'audit_regulation')

@admin.register(AuditSections)
class AuditSectionsAdmin(admin.ModelAdmin):
    search_fields = ['audit_type', 'section_number', 'section_heading']
    list_display = ('audit_type', 'section_number', 'section_heading')
    list_filter = ['audit_type', 'section_heading']

@admin.register(AuditQuestions)
class AuditQuestionsAdmin(admin.ModelAdmin):
    search_fields = ['section_num', 'subsection_num', 'section_text', 'subsection_text', 'general_question', 'audit_specific', 'audit_guidance' ]
    list_display = ('section_num', 'subsection_num', 'section_text', 'subsection_text', 'general_question', 'audit_specific', 'audit_guidance')
    list_filter = ['section_num','section_text','subsection_text']
    fieldsets = [
        ('Section',          {'fields': ['section_num',
                                        'section_text',
                                        'subsection_num',
                                        'subsection_text',
                                        ]}),
        ('Date information', {'fields': ['general_question',
                                        'audit_specific',
                                        'audit_guidance',
                                        ]}),
        ]
