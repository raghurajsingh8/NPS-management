# Generated by Django 5.0.3 on 2024-04-05 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autheticatweb', '0006_comment_dislike_like'),
    ]

    operations = [
        migrations.CreateModel(
            name='livechat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=300)),
            ],
        ),
        migrations.RemoveField(
            model_name='dislike',
            name='post',
        ),
        migrations.RemoveField(
            model_name='dislike',
            name='user',
        ),
        migrations.RemoveField(
            model_name='like',
            name='post',
        ),
        migrations.RemoveField(
            model_name='like',
            name='user',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Dislike',
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]