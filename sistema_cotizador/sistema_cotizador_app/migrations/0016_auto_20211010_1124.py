# Generated by Django 3.2.7 on 2021-10-10 16:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sistema_cotizador_app', '0015_auto_20211010_0858'),
    ]

    operations = [
        migrations.CreateModel(
            name='fichero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(auto_now_add=True)),
                ('nombre', models.CharField(max_length=100)),
                ('path', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='cotizador_maestro',
            name='id_usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='id_usuario', to=settings.AUTH_USER_MODEL, verbose_name='id_usuario'),
        ),
        migrations.AlterField(
            model_name='catalogo_ruc_dni',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='catalogo_tipo_cambio',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='cotizador_maestro',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='cotizador_maestro',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='ultima actualizacion'),
        ),
        migrations.AlterField(
            model_name='producto_servicio',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='fecha registro'),
        ),
        migrations.AlterField(
            model_name='producto_servicio',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='producto_servicio',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='multima actualizacion'),
        ),
        migrations.AlterField(
            model_name='producto_servicio',
            name='unidad_medida',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='producto_servicio',
            name='valor_neto',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
    ]