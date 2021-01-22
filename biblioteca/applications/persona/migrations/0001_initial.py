# Generated by Django 3.1.5 on 2021-01-21 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50, verbose_name='Nombres')),
                ('pais', models.CharField(max_length=30, verbose_name='Pais')),
                ('pasaporte', models.CharField(max_length=50, verbose_name='Pasaporte')),
                ('edad', models.IntegerField()),
                ('apelativo', models.CharField(max_length=50, verbose_name='Apelativos')),
            ],
            options={
                'verbose_name': 'Persona',
                'verbose_name_plural': 'Personas',
                'db_table': 'persona',
            },
        ),
        migrations.AddConstraint(
            model_name='persona',
            constraint=models.CheckConstraint(check=models.Q(edad__gte=18), name='edad_mayor_18'),
        ),
        migrations.AlterUniqueTogether(
            name='persona',
            unique_together={('pais', 'apelativo')},
        ),
    ]
