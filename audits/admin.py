from django.contrib import admin
from .models import AuditType, AuditSections, StandardWork

# to edit the columns visible in the admin view
# class AuditTypeAdmin(admin.ModelAdmin):


admin.site.register(AuditType)
admin.site.register(AuditSections)
admin.site.register(StandardWork)
