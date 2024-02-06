from django.db import models

class Comments(models.Model):
    name=models.CharField(max_length=50)
    comment=models.TextField()