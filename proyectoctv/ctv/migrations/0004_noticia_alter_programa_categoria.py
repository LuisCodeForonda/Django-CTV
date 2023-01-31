# Generated by Django 4.1.5 on 2023-01-30 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ctv', '0003_alter_programa_categoria'),
    ]

    operations = [
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('idtitulo', models.CharField(max_length=200, unique=True)),
                ('cuerpo', models.TextField()),
                ('subcategoria', models.CharField(choices=[('1', 'Sociedad'), ('2', 'Desastres y accidentes'), ('3', 'Seguridad'), ('4', 'Deportes'), ('5', 'Politica'), ('6', 'Entretenimiento')], default='Sociedad', max_length=1)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='programa',
            name='categoria',
            field=models.CharField(choices=[('1', 'Religiosos'), ('2', 'Noticieros'), ('3', 'Analisis'), ('4', 'Familiares'), ('5', 'Entretenimiento')], default='Religiosos', max_length=1, null=True),
        ),
    ]
