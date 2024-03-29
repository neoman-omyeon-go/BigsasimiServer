# Generated by Django 4.2.11 on 2024-03-29 16:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('debugtools', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-create_time']},
        ),
        migrations.AddField(
            model_name='blog',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='update_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
