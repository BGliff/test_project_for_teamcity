# Generated by Django 4.1.5 on 2023-01-24 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClientProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo_url', models.TextField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('date_of_birth', models.DateField(default=None, null=True)),
                ('gender', models.CharField(default=None, max_length=10, null=True)),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.clientprofile')),
            ],
        ),
    ]
