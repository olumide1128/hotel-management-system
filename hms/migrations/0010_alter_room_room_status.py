# Generated by Django 4.0.5 on 2022-08-09 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hms', '0009_alter_billing_billing_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='room_status',
            field=models.CharField(choices=[('Available', 'Available'), ('Occupied', 'Occupied'), ('Dirty', 'Dirty'), ('Booked', 'Booked'), ('Maintenance', 'Maintenance'), ('Inactive', 'Inactive')], max_length=15),
        ),
    ]
