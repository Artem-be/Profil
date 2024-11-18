# Generated by Django 5.1.1 on 2024-10-04 15:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_service_webdevelopment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hard_skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='WebDevelopmentHardSkills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('Hard_skills', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.hard_skills')),
            ],
        ),
    ]
