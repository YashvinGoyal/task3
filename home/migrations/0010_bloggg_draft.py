# Generated by Django 4.1 on 2023-06-25 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_remove_bloggg_draft'),
    ]

    operations = [
        migrations.AddField(
            model_name='bloggg',
            name='draft',
            field=models.BooleanField(default=False),
        ),
    ]
