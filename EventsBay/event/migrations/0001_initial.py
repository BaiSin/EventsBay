# Generated by Django 3.1.5 on 2021-02-27 05:33

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='eventlist',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('event_name', models.CharField(max_length=100)),
                ('data', models.CharField(max_length=500)),
                ('date', models.DateField()),
                ('location', models.CharField(max_length=35)),
                ('image', models.ImageField(upload_to='')),
                ('is_liked', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
