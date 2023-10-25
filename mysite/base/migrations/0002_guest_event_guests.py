# Generated by Django 4.2.6 on 2023-10-25 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('major', models.CharField(max_length=200, null=True)),
                ('person_type', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='guests',
            field=models.ManyToManyField(blank=True, related_name='guests', to='base.guest'),
        ),
    ]