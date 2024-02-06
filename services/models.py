from django.db import models
from tinymce.models import HTMLField
class Services(models.Model):
    icon=models.CharField(max_length=30)
    title=models.CharField(max_length=30)
    description=HTMLField()


