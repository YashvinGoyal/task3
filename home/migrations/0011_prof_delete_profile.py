# Generated by Django 4.1 on 2023-06-28 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_bloggg_draft'),
    ]

    operations = [
        migrations.CreateModel(
            name='prof',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=10)),
                ('lname', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=20)),
                ('uname', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=20)),
                ('img', models.FileField(default='', upload_to='')),
                ('address', models.CharField(max_length=20)),
                ('work', models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='profile',
        ),
    ]
