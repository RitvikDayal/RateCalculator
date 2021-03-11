from django.db import models

class excelFile(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    file = models.FileField(blank=True, null=True, upload_to='Excel_Files')

    def __str__(self):
        return self.title