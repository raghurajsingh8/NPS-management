# Generated by Django 5.0.3 on 2024-12-08 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autheticatweb', '0031_returneditem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='returneditem',
            name='serial_no',
            field=models.CharField(max_length=255),
        ),
    ]
