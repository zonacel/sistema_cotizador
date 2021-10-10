# Generated by Django 3.1.1 on 2021-10-10 13:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema_cotizador_app', '0012_auto_20211010_0842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalogo_ruc_dni',
            name='tipo_documento',
            field=models.PositiveIntegerField(max_length=2, validators=[django.core.validators.MaxValueValidator(99)]),
        ),
    ]
