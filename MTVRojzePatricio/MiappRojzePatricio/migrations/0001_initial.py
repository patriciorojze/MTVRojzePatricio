# Generated by Django 4.0.6 on 2022-07-31 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Familiares',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=35)),
                ('Apellido', models.CharField(max_length=35)),
                ('Edad', models.IntegerField()),
                ('FechaNacimiento', models.DateField()),
            ],
        ),
    ]
