# Generated by Django 5.0.3 on 2024-12-06 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autheticatweb', '0020_alter_purchase_date_alter_sale_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='box_type',
            field=models.CharField(choices=[('yes', 'YES'), ('no', 'NO'), ('N/A', 'N/A')], default='yes', max_length=50),
        ),
        migrations.AlterField(
            model_name='sale',
            name='box_type',
            field=models.CharField(choices=[('yes', 'YES'), ('no', 'NO'), ('N/A', 'N/A')], default='yes', max_length=50),
        ),
    ]
