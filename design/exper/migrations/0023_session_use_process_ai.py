# Generated by Django 3.1.4 on 2021-03-08 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exper', '0022_auto_20210221_2210'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='use_process_ai',
            field=models.BooleanField(default=False),
        ),
    ]
