# Generated by Django 3.2 on 2021-11-20 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in', models.DateField()),
                ('check_out', models.DateField()),
                ('booking_info', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='booking_info', to='listings.bookinginfo')),
                ('hotel_room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hotel_room', to='listings.hotelroom')),
            ],
        ),
    ]