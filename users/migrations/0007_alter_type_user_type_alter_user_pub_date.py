# Generated by Django 4.1.4 on 2022-12-27 23:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_type_user_type_alter_user_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='type',
            name='user_type',
            field=models.CharField(choices=[('Job Seeker', 'Job Seeker'), ('Job Provider', 'Job Provider')], max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 27, 23, 47, 16, 838823, tzinfo=datetime.timezone.utc)),
        ),
    ]
