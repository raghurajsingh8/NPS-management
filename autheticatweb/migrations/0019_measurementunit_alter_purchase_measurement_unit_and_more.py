# Generated by Django 5.0.3 on 2024-12-06 22:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autheticatweb', '0018_alter_purchase_measurement_unit_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MeasurementUnit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='purchase',
            name='measurement_unit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='purchases', to='autheticatweb.measurementunit'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='measurement_unit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sales', to='autheticatweb.measurementunit'),
        ),
    ]
