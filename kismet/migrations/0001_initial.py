# Generated by Django 4.1.5 on 2023-01-22 16:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Titel', models.CharField(max_length=100)),
                ('Beschreibung', models.CharField(max_length=300)),
                ('Adresse', models.CharField(max_length=100)),
                ('Mindestpreis', models.CharField(max_length=100)),
                ('Hoechstpreis', models.CharField(max_length=100)),
                ('maxGaesteanzahl', models.CharField(max_length=100)),
                ('Stadt', models.CharField(choices=[('Berlin', 'Berlin'), ('Bielefeld', 'Bielefeld'), ('Frankfurt', 'Frankfurt'), ('München', 'München'), ('Hamburg', 'Hamburg'), ('Köln', 'Köln')], default=0, max_length=15)),
                ('author', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
