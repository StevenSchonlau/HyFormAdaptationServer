# Generated by Django 3.0.5 on 2020-11-30 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ai', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='designer1',
            name='velocity',
            field=models.FloatField(default=0.1),
        ),
    ]