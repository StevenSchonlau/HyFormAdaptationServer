# Generated by Django 3.1.4 on 2021-10-19 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ai', '0003_designerbot_opsbot'),
    ]

    operations = [
        migrations.AddField(
            model_name='designerbot',
            name='channel_id',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='opsbot',
            name='channel_id',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]