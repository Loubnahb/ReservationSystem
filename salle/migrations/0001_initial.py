# Generated by Django 5.0 on 2023-12-28 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100, verbose_name="Nom de l'équipement")),
            ],
        ),
        migrations.CreateModel(
            name='Salle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100, verbose_name='Nom de la salle')),
                ('adresse', models.CharField(max_length=255, verbose_name='Adresse')),
                ('batiment_etage', models.CharField(max_length=100, verbose_name='Bâtiment/Étage')),
                ('etat', models.CharField(choices=[('disponible', 'Disponible'), ('maintenance', 'En maintenance')], default='disponible', max_length=100, verbose_name='État')),
                ('capacite', models.IntegerField(verbose_name='Capacité')),
                ('image', models.ImageField(blank=True, null=True, upload_to='salles_images/', verbose_name='Image')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('equipements', models.ManyToManyField(to='salle.equipement', verbose_name='Équipements')),
            ],
        ),
    ]
