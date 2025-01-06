# Generated by Django 5.1.4 on 2025-01-02 20:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_books', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'permissions': [('development', 'Permiso como Desarrollador'), ('scrum_master', 'Permiso como Scrum Master'), ('product_owner', 'Permiso como Product Owner')]},
        ),
        migrations.AlterField(
            model_name='accountuser',
            name='email',
            field=models.EmailField(error_messages={'unique': 'El correo electrónico ya está registrado. Por favor, usa otro.'}, max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=150, verbose_name='Autor'),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=150, verbose_name='Título'),
        ),
        migrations.AlterField(
            model_name='book',
            name='valuation',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10000)], verbose_name='Valoración'),
        ),
    ]