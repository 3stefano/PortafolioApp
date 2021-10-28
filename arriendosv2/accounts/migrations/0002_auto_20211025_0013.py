# Generated by Django 3.2.7 on 2021-10-25 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checkin',
            fields=[
                ('id_checkin', models.CharField(max_length=300, primary_key=True, serialize=False)),
                ('cuota2', models.IntegerField()),
                ('listacheck', models.CharField(max_length=300)),
            ],
            options={
                'db_table': 'checkin',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id_reserva', models.CharField(max_length=300, primary_key=True, serialize=False)),
                ('fechareserva', models.CharField(max_length=300)),
                ('cuota1', models.IntegerField()),
                ('pagototal', models.IntegerField()),
            ],
            options={
                'db_table': 'reserva',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ServiciosExtra',
            fields=[
                ('tipo_servicio', models.CharField(max_length=300, primary_key=True, serialize=False)),
                ('precio', models.IntegerField()),
            ],
            options={
                'db_table': 'servicios_extra',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='AuthGroup',
        ),
        migrations.DeleteModel(
            name='AuthGroupPermissions',
        ),
        migrations.DeleteModel(
            name='AuthPermission',
        ),
        migrations.DeleteModel(
            name='AuthUser',
        ),
        migrations.DeleteModel(
            name='AuthUserGroups',
        ),
        migrations.DeleteModel(
            name='AuthUserUserPermissions',
        ),
        migrations.DeleteModel(
            name='DjangoAdminLog',
        ),
        migrations.DeleteModel(
            name='DjangoContentType',
        ),
        migrations.DeleteModel(
            name='DjangoMigrations',
        ),
        migrations.DeleteModel(
            name='DjangoSession',
        ),
    ]