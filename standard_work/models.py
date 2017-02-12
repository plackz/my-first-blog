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

    work_title = models.CharField('title', max_length=200)
    work_frequency = models.CharField(max_length=1, choices=WORK_FREQ)
    work_last_dt = models.DateField('last date', null=True, blank=True,)
    work_next_dt = models.DateField('next sched date', null=True, blank=True)

    def __str__(self):
        return self.work_title

    # TODO: add function to calculate next check date based on frequency

    class Meta:
        verbose_name = 'Standard work'
        verbose_name_plural = 'Standard work'

class WorkGuidance(models.Model):
    guide_title = models.ForeignKey(StandardWork)
    guide_text = models.TextField()

    def __str__(self):
        return self.guide_text

    class Meta:
        verbose_name = 'Work guidance'
        verbose_name_plural = 'Work guidance'


class WorkRemarks(models.Model):
    remark_title = models.ForeignKey(StandardWork)
    # FIX: find a way to list the steps from the guidance table. 
    remark_guide = models.ForeignKey(WorkGuidance)
    remark_text = models.TextField()
    remark_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.remark_text

    class Meta:
        verbose_name = 'Records'
        verbose_name_plural = 'Records'
