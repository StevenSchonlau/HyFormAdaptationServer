# Generated by Django 3.0.2 on 2020-02-14 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exper', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='study',
            name='lead',
            field=models.CharField(default='no one', max_length=50),
        ),
    ]
