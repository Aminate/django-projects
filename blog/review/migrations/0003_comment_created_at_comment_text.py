# Generated by Django 4.2 on 2023-04-14 08:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2023, 4, 14, 8, 56, 45, 388167, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='text',
            field=models.TextField(default=datetime.datetime(2023, 4, 14, 8, 57, 4, 578573, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
    ]
