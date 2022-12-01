# Generated by Django 4.1.3 on 2022-12-01 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('familiares', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Celular',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('modelo', models.CharField(max_length=50)),
                ('marca', models.CharField(max_length=50)),
                ('fecha_lanzamiento', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Paquete',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('peso', models.IntegerField()),
                ('remitente', models.CharField(max_length=50)),
                ('destinatario', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('edad', models.IntegerField()),
                ('fecha_nacimiento', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='Familiar',
        ),
    ]
