from django.db import models
from django.utils import timezone

class StandardWork(models.Model):
    WORK_FREQ = (
        ('D', 'Daily'),
        ('W', 'Weekly'),
        ('B', 'Bi-Monthly (2x Mo.)'),
        ('M', 'Monthly'),
        ('Q', 'Quarterly'),
        ('Y', 'Yearly'),
    )

    work_title = models.CharField(max_length=200)
    work_frequency = models.CharField(max_length=1, choices=WORK_FREQ)
    work_last_dt = models.DateField(null=True, blank=True,)
    work_next_dt = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.work_title

    # TODO: add function to calculate next check date based on frequency
