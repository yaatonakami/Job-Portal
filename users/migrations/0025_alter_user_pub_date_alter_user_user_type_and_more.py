# Generated by Django 4.1.4 on 2022-12-28 10:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0024_alter_user_pub_date_alter_user_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 28, 10, 49, 26, 239882, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('Job Provider', 'Job Provider'), ('Job Seeker', 'Job Seeker')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, max_length=200, verbose_name='Username'),
        ),
    ]
