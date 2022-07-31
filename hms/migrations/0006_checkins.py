# Generated by Django 4.0.5 on 2022-07-20 17:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hms', '0005_guest_reservation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checkins',
            fields=[
                ('checkin_id', models.AutoField(primary_key=True, serialize=False)),
                ('checkin_date', models.DateField()),
                ('checkout_date', models.DateField()),
                ('Num_of_persons', models.IntegerField()),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hms.guest')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hms.room')),
            ],
        ),
    ]