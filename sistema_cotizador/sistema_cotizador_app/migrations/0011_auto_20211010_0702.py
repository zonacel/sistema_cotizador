# Generated by Django 3.1.1 on 2021-10-10 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema_cotizador_app', '0010_auto_20211010_0641'),
    ]

    operations = [
        migrations.CreateModel(
            name='catalogo_tipo_cambio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(auto_now_add=True)),
                ('compra', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('venta', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('origen', models.CharField(max_length=100)),
                ('moneda', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='cotizador_maestro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='fecha reigstro')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='ultima actualizadcion')),
                ('nombre_proyecto', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='catalogo_ruc_dni',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
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