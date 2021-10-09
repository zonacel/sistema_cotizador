# Generated by Django 3.2.7 on 2021-10-09 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema_cotizador_app', '0003_producto_servicio'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto_servicio',
            name='status',
            field=models.BooleanField(default=True, verbose_name='estado'),
        ),
        migrations.AddField(
            model_name='producto_servicio',
            name='valor_neto',
            field=models.DecimalField(decimal_places=2, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='creado'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='modificado'),
        ),
        migrations.AlterField(
            model_name='producto_servicio',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='creado'),
        ),
        migrations.AlterField(
            model_name='producto_servicio',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='modificado'),
        ),
    ]
