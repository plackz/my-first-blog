from django.contrib import admin
from .models import AuditType, AuditSections, AuditQuestions, AuditComments

@admin.register(AuditType)
class AuditTypeAdmin(admin.ModelAdmin):
    list_display = ('type_title', 'audit_type_fld', 'audit_regulation')

@admin.register(AuditSections)
class AuditSectionsAdmin(admin.ModelAdmin):
    search_fields = ['audit_type', 'section_number', 'section_heading']
    list_display = ('audit_type', 'section_number', 'section_heading')
    list_filter = ['audit_type', 'section_heading']

@admin.register(AuditComments)
class AuditCommentsAdmin(admin.ModelAdmin):
    search_fields = ['comment_title', 'comment_text', 'sap_ref']
    list_display = ('question_num', 'auditor_name', 'finding', 'comment_title', 'comment_text', 'sap_ref' )
    list_filter = []

class AuditCommentsInlineAdmin(admin.TabularInline):
    model = AuditComments

    def get_extra (self, request, obj=None, **kwargs):
        """Dynamically sets the number of extra forms. 0 if the related object
        already exists or the extra configuration otherwise."""
        if obj:
            # Don't add any extra forms if the related object already exists.
            return 0
        return self.extra

@admin.register(AuditQuestions)
class AuditQuestionsAdmin(admin.ModelAdmin):
    search_fields = ['section_num', 'subsection_num', 'section_text', 'subsection_text', 'general_question', 'audit_specific', 'audit_guidance' ]
    list_display = ('question_id', 'section_num', 'subsection_num', 'section_text', 'subsection_text', 'general_question', 'audit_specific', 'audit_guidance')
    ordering = ('subsection_num',) # The positive sign indicates ascending order
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
    inlines = [ AuditCommentsInlineAdmin ]
