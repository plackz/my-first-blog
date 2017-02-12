from django.db import models
from django.utils import timezone

class AuditType(models.Model):
    AUDIT_TYPES = (
        ('ISO', 'ISO 9001'),
        ('API', 'API 6D and 6A'),
        ('PED', 'PED'),
        ('DNV', 'DNV'),
        ('EAC', 'Russian Certification'),
        ('ABS', 'ABS'),
        ('Cust', 'Customer audit'),
    )

    AUDIT_REG = (
        ('ISO', 'ISO 9001:2015'),
        ('API', 'API 6D, 6A, Q1, 607'),
        ('PED', 'EU 2014/68'),
        ('Cust', 'Customer specification'),
        ('TBD', 'To be determined'),
    )

    type_title = models.CharField(max_length=50)
    audit_type_fld = models.CharField('audit type', max_length=4, choices=AUDIT_TYPES)
    audit_regulation = models.CharField(max_length=4, choices=AUDIT_REG)

    def __str__(self):
        return self.type_title


# TODO: finish audit sections table
class AuditSections(models.Model):
    audit_type = models.ForeignKey('AuditType')
    section_number = models.CharField(max_length=10)
    section_heading = models.CharField(max_length=50)

    def __str__(self):
        return self.section_heading

    class Meta:
        verbose_name = 'Audit section'
        verbose_name_plural = 'Audit sections'



'''
# TODO: create audit record
class AuditRecord(modles.Model):
    audit_id = models.AutoField(primary_key=True)
    audit_title = modles.CharField(max_length=200)
    last_audit_date = models.DateField("date of last audit", blank=True, null=True)
    next_sched_date = modles.DateField("next scheduled date", blank=True, null=True)
    # TODO: can I have more than one Foreign key? need users, audit type, audit sections
    audit_type_record = models.ForeignKey('AuditType')
    lead_auditor = modles.ForeignKey('auth.User')
    external_auditor = models.CharField(max_length=200)
    # TODO: figure out how to have a selection of several different sections. need a multi choice selection
    audit_scope = models.ForeignKey('AuditSections')
    # TODO: audit findings
    # audit_finding_list = ('AuditFindings')
    # TODO: create a method to filter on upcomming audit in 30d and also 90d
    def

# TODO: create AuditFindings
class AuditFindings(models.Model):
    AUDIT_STATUS = (
        ('O', 'Open'),
        ('R', 'Pending Review'),
        ('C', 'Closed'),
    )

    audit_finding_title = CharField(max_length=200)
    audit_finding_auditor = # TODO: which field? want to auto generate from the person typing
    audit_finding_date = models.DateField(default=timezone.now)
    audit_status = models.CharField(max_length=1, choices=AUDIT_STATUS)
    audit_finding_text = models.TextField()
    audit_applies_to = models.ForeignKey('AuditRecord')

'''
