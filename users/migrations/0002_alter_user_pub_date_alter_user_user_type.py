# Generated by Django 4.1.4 on 2022-12-27 09:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 27, 9, 29, 6, 902110, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('Job Provider', 'Job Provider'), ('Job Seeker', 'Job Seeker')], max_length=100, null=True),
        ),
    ]