# Generated by Django 3.2.7 on 2021-10-10 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sistema_cotizador_app', '0018_auto_20211010_1138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cotizador_detalle',
            name='id_cotizador_maestro',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sistema_cotizador_app.cotizador_maestro', verbose_name='id cotizador maestro'),
        ),
    ]
