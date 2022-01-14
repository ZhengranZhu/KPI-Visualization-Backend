# Generated by Django 2.2 on 2021-12-30 03:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DimDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StartDateKey', models.CharField(max_length=10, unique=True)),
                ('CalendarYear', models.IntegerField()),
                ('MonthOfYear', models.IntegerField()),
                ('WeekOfYear', models.IntegerField(null=True)),
                ('MonthName', models.CharField(max_length=20)),
                ('DayOfMonth', models.IntegerField()),
                ('DayOfWeek', models.IntegerField()),
                ('DayName', models.CharField(max_length=20)),
                ('FiscalYear', models.IntegerField()),
                ('FiscalQuarter', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='DimProductFamily',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProductFamilyKey', models.CharField(max_length=20, unique=True)),
                ('ProductDescriptionEn', models.CharField(max_length=500, null=True)),
                ('StandardManufacturingTime', models.FloatField(null=True)),
                ('CncStandardTime', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ErrorSerialNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SerialNumber', models.CharField(max_length=20)),
                ('IsCreated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductionOrders',
            fields=[
                ('OrderNumber', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('DateAndTime', models.DateTimeField()),
                ('Quantity', models.IntegerField()),
                ('Destination', models.CharField(max_length=30)),
                ('OrderDate', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='CncOrder', to='Data_aquisition.DimDate', to_field='StartDateKey')),
            ],
        ),
        migrations.CreateModel(
            name='ProductionLineAttendanceFact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ShAssembly', models.FloatField()),
                ('ScAssembly', models.FloatField()),
                ('ScrAssembly', models.FloatField()),
                ('AluMskAssembly', models.FloatField()),
                ('Cnc', models.FloatField()),
                ('Assembly', models.FloatField()),
                ('All', models.FloatField()),
                ('Date', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='AttendanceAssPerson', to='Data_aquisition.DimDate', to_field='StartDateKey')),
            ],
        ),
        migrations.CreateModel(
            name='ManufacturingFact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SerialNumber', models.CharField(max_length=20, unique=True)),
                ('MaterialNumber', models.CharField(max_length=10, null=True)),
                ('SalesOrderNumber', models.CharField(max_length=10, null=True)),
                ('Plant', models.CharField(max_length=10, null=True)),
                ('ProductionLine', models.CharField(max_length=10, null=True)),
                ('PreassemblyStartTime', models.DateTimeField()),
                ('WashingStartTime', models.DateTimeField()),
                ('PackagingStartTime', models.DateTimeField()),
                ('CncThroughputTime', models.FloatField(null=True)),
                ('AssThroughputTime', models.FloatField(null=True)),
                ('AllThroughputTime', models.FloatField(null=True)),
                ('PackagingStartDateKey', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='Testing', to='Data_aquisition.DimDate', to_field='StartDateKey')),
                ('PreassemblyStartDateKey', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='Preassembly', to='Data_aquisition.DimDate', to_field='StartDateKey')),
                ('ProductFamilyKey', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='Family', to='Data_aquisition.DimProductFamily', to_field='ProductFamilyKey')),
                ('WashingStartDateKey', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='Washing', to='Data_aquisition.DimDate', to_field='StartDateKey')),
            ],
        ),
        # migrations.CreateModel(
        #     name='AttendanceCncFact',
        #     fields=[
        #         ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        #         ('Pers_No', models.CharField(max_length=50, null=True)),
        #         ('CC', models.CharField(max_length=100, null=True)),
        #         ('Description', models.CharField(max_length=100)),
        #         ('Attendance_Time', models.FloatField(null=True)),
        #         ('Date', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='AttendanceCNCPerson', to='Data_aquisition.DimDate', to_field='StartDateKey')),
        #     ],
        # ),
        # migrations.CreateModel(
        #     name='AttendanceAssFact',
        #     fields=[
        #         ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        #         ('Pers_No', models.CharField(max_length=50, null=True)),
        #         ('CC', models.CharField(max_length=100, null=True)),
        #         ('Description', models.CharField(max_length=100)),
        #         ('Attendance_Time', models.FloatField(null=True)),
        #         ('Date', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='AttendancePerson', to='Data_aquisition.DimDate', to_field='StartDateKey')),
        #     ],
        # ),
    ]
