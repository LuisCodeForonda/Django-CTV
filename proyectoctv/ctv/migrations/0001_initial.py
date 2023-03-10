# Generated by Django 4.1.5 on 2023-01-26 23:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Programacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hora_emision', models.TimeField()),
                ('nombre', models.CharField(max_length=100)),
                ('dias', models.CharField(choices=[('1', 'Lunes a Viernes'), ('2', 'Sabados'), ('3', 'Domingos')], default='Lunes a Viernes', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Programa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('imagen', models.ImageField(null=True, upload_to='programasimg')),
                ('hora_inicio', models.TimeField()),
                ('hora_fin', models.TimeField()),
                ('descripcion', models.TextField(blank=True, max_length=200)),
                ('link_facebook', models.CharField(blank=True, max_length=100)),
                ('link_twitter', models.CharField(blank=True, max_length=100)),
                ('link_instagram', models.CharField(blank=True, max_length=100)),
                ('link_tiktok', models.CharField(blank=True, max_length=100)),
                ('link_youtube', models.CharField(blank=True, max_length=100)),
                ('categoria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ctv.categoria')),
            ],
        ),
    ]
