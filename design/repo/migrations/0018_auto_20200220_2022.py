# Generated by Django 3.0.2 on 2020-02-20 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('repo', '0017_profile_is_exper'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plan',
            name='paths',
        ),
        migrations.RemoveField(
            model_name='waypoint',
            name='group',
        ),
        migrations.RemoveField(
            model_name='waypoint',
            name='session',
        ),
        migrations.AddField(
            model_name='path',
            name='plan',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='repo.Plan'),
        ),
    ]
