from django.db import models

class Visit(models.Model):
    useragent = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)