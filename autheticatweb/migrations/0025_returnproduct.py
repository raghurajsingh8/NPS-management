# Generated by Django 5.0.3 on 2024-12-07 21:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autheticatweb', '0024_alter_purchase_category_alter_sale_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReturnProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sale_to', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('measurement_unit', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=100)),
                ('serial_no', models.CharField(max_length=100)),
                ('box_type', models.CharField(blank=True, max_length=100, null=True)),
                ('date', models.DateField()),
                ('verified_by', models.CharField(max_length=100)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autheticatweb.product')),
            ],
        ),
    ]
