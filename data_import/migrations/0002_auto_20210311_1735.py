# Generated by Django 3.1.7 on 2021-03-11 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_import', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='excelfile',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='Excel_Files'),
        ),
    ]