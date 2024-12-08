# Generated by Django 5.0.3 on 2024-12-08 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autheticatweb', '0030_delete_rowstate'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReturnedItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_no', models.CharField(max_length=255, unique=True)),
                ('returned_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
