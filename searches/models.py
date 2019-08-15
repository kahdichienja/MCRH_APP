from django.db import models
from Mcrh_Birth_Record.models import Child, Parent

# Create your models here.

class SearchQuery(models.Model):
    child = models.ForeignKey(Child, blank=True, null=True,  on_delete=models.SET_NULL)
    query = models.CharField(max_length = 220)
    timestamp = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.query
