# Generated by Django 2.1.2 on 2019-02-12 11:35

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
                ('description', models.CharField(blank=True, default='', max_length=200)),
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
                ('tag', models.CharField(max_length=100, unique=True)),
                ('description', models.CharField(blank=True, default='', max_length=200)),
                ('type', models.CharField(choices=[('INPUT', 'Input'), ('OUTPUT', 'Output')], default='INPUT', max_length=32)),
                ('on_description', models.CharField(blank=True, default='On', max_length=200)),
                ('off_description', models.CharField(blank=True, default='Off', max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Digital IO',
            },
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=100, unique=True)),
                ('description', models.CharField(blank=True, default='', max_length=200)),
                ('revision', models.FloatField(default=-1.0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DocumentEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(auto_created=True, unique=True)),
                ('text', models.TextField(blank=True, default='', max_length=500)),
            ],
            options={
                'verbose_name_plural': 'Document Entries',
            },
        ),
        migrations.CreateModel(
            name='DocumentSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=100, unique=True)),
                ('description', models.CharField(blank=True, default='', max_length=200)),
                ('hierarchy', models.PositiveSmallIntegerField(choices=[(1, 'Level 1'), (2, 'Level 2'), (3, 'Level 3'), (4, 'Level 4')])),
                ('order', models.PositiveIntegerField(blank=True, null=True)),
                ('section_number', models.CharField(blank=True, max_length=32, null=True)),
                ('assigned_document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tables.Document')),
                ('assigned_section', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tables.DocumentSection')),
            ],
            options={
                'verbose_name_plural': 'Document Sections',
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
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('CUSTOM', 'Custom'), ('FLT', 'Fault'), ('ON', 'On'), ('OFF', 'Off'), ('HH', 'High High'), ('H', 'High'), ('L', 'Low'), ('LL', 'Low Low'), ('FAIL_TO_START', 'Fail to Start'), ('FAIL_TO_STOP', 'Fail to Stop'), ('FAIL_TO_OPEN', 'Fail to Open'), ('FAIL_TO_CLOSE', 'Fail to Close'), ('FBK_FAIL', 'Feedback Fail'), ('COM_FAIL', 'Communications Fail')], default='ON', max_length=200)),
                ('alarm_enable', models.BooleanField(default=False)),
                ('priority', models.PositiveSmallIntegerField(choices=[(1, 'Critical'), (2, 'High'), (3, 'Medium'), (4, 'Low')], default=4)),
            ],
        ),
        migrations.CreateModel(
            name='IndexTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=100, unique=True)),
                ('table', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Instrument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=100, unique=True)),
                ('description', models.CharField(blank=True, default='', max_length=200)),
                ('io_allocation', models.CharField(blank=True, default='', max_length=100)),
                ('cabinet', models.CharField(blank=True, default='', max_length=100)),
                ('pid_doc', models.CharField(blank=True, default='', max_length=500)),
                ('schematic_doc', models.CharField(blank=True, default='', max_length=500)),
                ('termination_doc', models.CharField(blank=True, default='', max_length=500)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AnalogIO',
            fields=[
                ('instrument_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='tables.Instrument')),
                ('type', models.CharField(choices=[('INPUT', 'Input'), ('OUTPUT', 'Output')], default='INPUT', max_length=32)),
                ('range', models.CharField(blank=True, default='0-100', max_length=32)),
                ('units', models.CharField(blank=True, default='', max_length=32)),
                ('hh_sp', models.FloatField(blank=True, default=95.0, verbose_name='High High Setpoint')),
                ('h_sp', models.FloatField(blank=True, default=90.0, verbose_name='High Setpoint')),
                ('l_sp', models.FloatField(blank=True, default=10.0, verbose_name='Low Setpoint')),
                ('ll_sp', models.FloatField(blank=True, default=5.0, verbose_name='Low Low Setpoint')),
                ('hysteresis', models.FloatField(blank=True, default=1.0, verbose_name='Hysteresis')),
            ],
            options={
                'verbose_name_plural': 'Analog IO',
            },
            bases=('tables.instrument',),
        ),
        migrations.AddField(
            model_name='instrument',
            name='index_tag',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tables.IndexTag'),
        ),
        migrations.AddField(
            model_name='documentsection',
            name='index_tag',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tables.IndexTag'),
        ),
        migrations.AddField(
            model_name='documententry',
            name='assigned_section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tables.DocumentSection'),
        ),
        migrations.AddField(
            model_name='document',
            name='index_tag',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tables.IndexTag'),
        ),
        migrations.AddField(
            model_name='digitalio',
            name='index_tag',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tables.IndexTag'),
        ),
    ]
