# Generated by Django 3.1.1 on 2021-10-09 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema_cotizador_app', '0008_alter_cliente_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='producto_servicio',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
