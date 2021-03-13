from django.db import models
from django.utils import timezone
from django.urls import reverse

class excelFile(models.Model):
    file = models.FileField(blank=True, null=True, upload_to='Excel_Files')
    date_uploaded = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.date_uploaded
    
    def get_absolute_url(self):
        return reverse("home", kwargs={"pk": self.pk})


