from django.db import models
from django.utils import timezone
import datetime
from django.utils.timesince import timesince

class Incidents(models.Model):
    incident_title = models.CharField(max_length=200)
    incident_text = models.TextField()
    customer_affected = models.BooleanField()
    incident_contact = models.CharField(max_length=200)
    incident_dt = models.DateTimeField('incident date')
    resolution_dt = models.DateTimeField('completed date', blank=True, null=True)
    root_cause = models.TextField()
    steps_to_fix = models.TextField()
    resolved_time = models.IntegerField('duration (in minutes)')
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.incident_title

    '''
    def time_to_resolve(self):
        "Returns the time it took to resolve the incident"
        dummydate = datetime.date(2000, 1, 1) # Needed to convert time to a datetime object
        dt1 = datetime.combine(dummydate, self.incident_dt)
        dt2 = datetime.combine(dummydate, self.resolution_dt)
        return timesince(dt1, dt2) # Assuming dt2 is the more recent time
    resolved_time = property(time_to_resolve)
    '''

    class Meta:
        verbose_name = 'Incidents'
        verbose_name_plural = 'Incidents'
