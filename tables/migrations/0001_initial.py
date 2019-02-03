# Generated by Django 2.1.2 on 2019-02-02 03:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alarm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=100, unique=True)),
                ('description', models.CharField(max_length=200)),
                ('type', models.CharField(choices=[('D', 'Digital'), ('HH', 'High High'), ('H', 'High'), ('L', 'Low'), ('LL', 'Low Low')], default='D', max_length=32)),
                ('priority', models.PositiveSmallIntegerField(choices=[(1, 'Critical'), (2, 'High'), (3, 'Medium'), (4, 'Low')], default=4)),
                ('refObject', models.CharField(blank=True, default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CtrlObject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=100, unique=True)),
                ('description', models.CharField(blank=True, default='', max_length=200)),
                ('type', models.CharField(choices=[('DI', 'Digital Input'), ('DO', 'Digital Output'), ('AI', 'Analog Input'), ('AO', 'Analog Output'), ('DRiVE', 'Drive'), ('VALVE', 'Valve')], max_length=32)),
            ],
            options={
                'verbose_name_plural': 'Control Objects',
            },
        ),
        migrations.CreateModel(
            name='DigitalIO',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('on_description', models.CharField(default='On', max_length=100)),
                ('off_description', models.CharField(default='Off', max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Digital IO',
            },
        ),
        migrations.CreateModel(
            name='Drive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Instrument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('io_allocation', models.CharField(blank=True, default='', max_length=100)),
                ('cabinet', models.CharField(blank=True, default='', max_length=200)),
                ('pid_doc', models.CharField(blank=True, default='', max_length=200)),
                ('schematic_doc', models.CharField(blank=True, default='', max_length=200)),
                ('termination_doc', models.CharField(blank=True, default='', max_length=200)),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tables.CtrlObject')),
            ],
        ),
        migrations.AddField(
            model_name='digitalio',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tables.Instrument'),
        ),
    ]
