# Generated by Django 3.0.8 on 2020-09-09 10:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exper', '0018_auto_20200909_1002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='experiment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='exper.Experiment'),
        ),
    ]