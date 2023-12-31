# Generated by Django 4.2.6 on 2023-10-25 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_guest_event_guests'),
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_id', models.IntegerField(default=-1, null=True)),
                ('max_seats', models.IntegerField(default=-1, null=True)),
                ('label', models.CharField(max_length=200, null=True)),
                ('seated_guests', models.ManyToManyField(blank=True, related_name='seated_guests', to='base.guest')),
            ],
        ),
        migrations.CreateModel(
            name='SeatingChart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tables', models.ManyToManyField(blank=True, related_name='tables', to='base.table')),
            ],
        ),
    ]
