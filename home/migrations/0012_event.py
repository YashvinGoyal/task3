# Generated by Django 4.1 on 2023-06-28 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_prof_delete_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='event',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=15)),
                ('dso', models.TextField()),
                ('pso', models.TextField()),
                ('date', models.DateField(default='')),
                ('stime', models.TimeField(default='')),
                ('endt', models.TimeField(default='')),
                ('special', models.CharField(max_length=20)),
            ],
        ),
    ]
