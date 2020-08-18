from django.db import models
from django.conf import settings


class DemoVideos(models.Model):
    MODULE_CHOICES = (
        ('1', 'module_1'),
        ('2', 'module_2'),
        ('3', 'module_3'),
        ('4', 'module_4'),
    )
    module_name = models.CharField(max_length=1, blank=False, null=False, choices=MODULE_CHOICES)
    video = models.FileField(null=True)

    def __str__(self):
        return "{}".format(self.module_name)


class ModuleScript(models.Model):
    MODULE_CHOICES = (
        ('1', 'module_1'),
        ('2', 'module_2'),
        ('3', 'module_3'),
        ('4', 'module_4'),
    )
    module_name = models.CharField(max_length=1, blank=True, null=True, choices=MODULE_CHOICES)
    text = models.CharField(max_length=2056, null=False, blank=False)

    def __str__(self):
        return "{}".format(self.module_name)
