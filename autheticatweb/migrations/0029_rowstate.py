# Generated by Django 5.0.3 on 2024-12-08 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autheticatweb', '0028_delete_return'),
    ]

    operations = [
        migrations.CreateModel(
            name='RowState',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('row_id', models.CharField(max_length=100, unique=True)),
                ('is_yellow', models.BooleanField(default=False)),
            ],
        ),
    ]
