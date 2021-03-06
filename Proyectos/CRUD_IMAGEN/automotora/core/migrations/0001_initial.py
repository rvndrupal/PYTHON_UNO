# Generated by Django 2.2.7 on 2019-12-26 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Automovil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patente', models.CharField(max_length=50, unique=True)),
                ('modelo', models.CharField(max_length=50)),
                ('anio', models.IntegerField()),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Marca')),
            ],
        ),
    ]
