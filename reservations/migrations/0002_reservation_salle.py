# Generated by Django 5.0 on 2023-12-30 22:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0001_initial'),
        ('salle', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='salle',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='salle.salle'),
        ),
    ]
