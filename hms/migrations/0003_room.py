# Generated by Django 4.0.5 on 2022-07-16 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hms', '0002_employee_access_granted'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('room_num', models.AutoField(primary_key=True, serialize=False)),
                ('room_type', models.CharField(choices=[('Single', 'Single'), ('Double', 'Double'), ('Deluxe', 'Deluxe'), ('Twin', 'Twin'), ('Executive', 'Executive')], max_length=15)),
                ('room_price', models.FloatField()),
                ('room_status', models.CharField(choices=[('Available', 'Available'), ('Occupied', 'Occupied'), ('Dirty', 'Dirty'), ('Booked', 'Booked')], max_length=15)),
            ],
        ),
    ]