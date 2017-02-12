from django.contrib import admin
from .models import StandardWork

# to edit the columns visible in the admin view
# class AuditTypeAdmin(admin.ModelAdmin):

admin.site.register(StandardWork)
