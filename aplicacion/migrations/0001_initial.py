# Generated by Django 5.1.3 on 2024-11-26 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiantes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('año', models.IntegerField()),
                ('division', models.CharField(max_length=1)),
                ('inasistencias', models.DecimalField(decimal_places=1, max_digits=2)),
                ('fecha_de_nacimiento', models.DateField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('inasistencias', models.DecimalField(decimal_places=1, max_digits=2)),
                ('fecha_de_nacimiento', models.DateField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]