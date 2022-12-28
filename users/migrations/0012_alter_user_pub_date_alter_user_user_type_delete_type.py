# Generated by Django 4.1.4 on 2022-12-28 00:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_alter_type_user_type_alter_user_pub_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 28, 0, 30, 30, 425975, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('Job Provider', 'Job Provider'), ('Job Seeker', 'Job Seeker')], max_length=100, null=True, unique=True),
        ),
        migrations.DeleteModel(
            name='Type',
        ),
    ]