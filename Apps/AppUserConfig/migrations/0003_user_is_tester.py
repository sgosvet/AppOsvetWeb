# Generated by Django 3.0.4 on 2021-06-03 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppUserConfig', '0002_auto_20210603_1347'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_tester',
            field=models.BooleanField(default=False),
        ),
    ]
