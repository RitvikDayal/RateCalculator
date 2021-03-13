# Utility import
from django.db import models
from django.utils import timezone
from django.urls import reverse


# Models to log the file uploads.
class excelFile(models.Model):
    '''
    creates a table with 3 columns: Id, file, date_uploaded
    Id: auto generated primary_key.
    file: file name uploaded to the database.
    date_uploaded: timestamp of the upload.
    '''
    file = models.FileField(blank=True, null=True, upload_to='Excel_Files') # File Column
    date_uploaded = models.DateTimeField(default=timezone.now) # Timestamp Column

    def __str__(self):
        return self.date_uploaded
    
    # Reverse route for login authentication
    def get_absolute_url(self):
        return reverse("home", kwargs={"pk": self.pk})


