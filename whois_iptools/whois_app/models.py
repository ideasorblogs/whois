from django.db import models

# Create your models here.


class SearchTerm(models.Model):
    keywords = models.CharField(max_length=500, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    count = models.PositiveIntegerField(default=0)
    ses_id = models.CharField(max_length=100, null=True, blank=True)
    ip = models.GenericIPAddressField(default='127.0.0.1')

    def __str__(self):
        return self.keywords