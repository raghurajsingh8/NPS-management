# Generated by Django 5.0.3 on 2024-12-06 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autheticatweb', '0021_alter_purchase_box_type_alter_sale_box_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='box_type',
            field=models.CharField(choices=[('yes', 'YES'), ('no', 'NO'), ('Not Applicable', 'Not Applicable')], default='yes', max_length=50),
        ),
        migrations.AlterField(
            model_name='sale',
            name='box_type',
            field=models.CharField(choices=[('yes', 'YES'), ('no', 'NO'), ('Not Applicable', 'Not Applicable')], default='yes', max_length=50),
        ),
    ]