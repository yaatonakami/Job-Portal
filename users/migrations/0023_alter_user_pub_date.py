# Generated by Django 4.1.4 on 2022-12-28 10:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0022_remove_user_is_active_alter_user_pub_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 28, 10, 39, 4, 625934, tzinfo=datetime.timezone.utc)),
        ),
    ]
