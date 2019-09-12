from django.db import models
from datetime import datetime
# Create your models here.

class posting(models.Model):
    posting_title = models.CharField(max_length= 50)
    posting_context = models.TextField()
    posting_date = models.DateTimeField("date posted", default = datetime.now())

    def __str__(self):
        return self.posting_title
