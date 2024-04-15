# Generated by Django 4.2.11 on 2024-04-11 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0003_userprofile_goals_natrium_alter_userprofile_avatar'),
    ]

    operations = [
        migrations.CreateModel(
            name='IngestionInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('image_path', models.TextField(blank=True, default='/static/image/default_image.png', null=True)),
                ('name', models.CharField(default='None', max_length=256)),
                ('calories', models.PositiveIntegerField(default=0)),
                ('carb', models.PositiveIntegerField(default=0)),
                ('protein', models.PositiveIntegerField(default=0)),
                ('fat', models.PositiveIntegerField(default=0)),
                ('natrium', models.PositiveIntegerField(default=0)),
                ('trans_fat', models.PositiveIntegerField(default=0)),
                ('saturated_fat', models.PositiveIntegerField(default=0)),
                ('unsaturated_fat', models.PositiveIntegerField(default=0)),
                ('cholesterol', models.PositiveIntegerField(default=0)),
                ('userprofile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingestion_info', to='account.userprofile')),
            ],
        ),
    ]