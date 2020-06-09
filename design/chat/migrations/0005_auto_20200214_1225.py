# Generated by Django 3.0.2 on 2020-02-14 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exper', '0001_initial'),
        ('chat', '0004_auto_20200213_2048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='structure',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exper.Structure'),
        ),
        migrations.AlterField(
            model_name='channelposition',
            name='position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exper.Position'),
        ),
    ]
