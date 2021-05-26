from django.db import models

# Create your models here.
class targets(models.Model):
    target_id = models.IntegerField(primary_key=True,blank=False,null=False)
    route_id = models.IntegerField()
    item_code = models.CharField(max_length=25)
    item_description = models.CharField(max_length=150)
    month_target = [('JAN','JANUARY'),
                    ('FEB','FEBRUARY'),
                    ('MAR','MARCH'),
                    ('APR','APRIL'),
                    ('MAY','MAY'),
                    ('JUN','JUNE'),
                    ('JUL','JULY'),
                    ('AUG','AUGUST'),
                    ('SEPT','SEPTEMBER'),
                    ('OCT','OCTOBER'),
                    ('NOV','NOVEMEBER'),
                    ('DEC','DECEMBER')]
    TARGET_MONTH = models.CharField(max_length=5,
                                    choices=month_target,
                                    default='JAN')
    WORKINGDAYS = models.IntegerField(default = 26)
    
    class Meta:
        verbose_name_plural = "targets"
    