# Generated by Django 5.0.1 on 2024-01-23 15:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_reservation_event_reservations'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.URLField()),
                ('description', models.TextField()),
                ('venue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='main_app.venue')),
            ],
        ),
    ]