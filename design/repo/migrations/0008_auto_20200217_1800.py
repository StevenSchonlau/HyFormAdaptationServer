# Generated by Django 3.0.2 on 2020-02-17 18:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('exper', '0004_auto_20200214_1254'),
        ('repo', '0007_auto_20200214_1514'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datalog',
            name='team',
        ),
        migrations.RemoveField(
            model_name='path',
            name='team',
        ),
        migrations.RemoveField(
            model_name='plan',
            name='team',
        ),
        migrations.RemoveField(
            model_name='scenario',
            name='team',
        ),
        migrations.RemoveField(
            model_name='target',
            name='team',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='team',
        ),
        migrations.RemoveField(
            model_name='warehouse',
            name='team',
        ),
        migrations.RemoveField(
            model_name='waypoint',
            name='team',
        ),
        migrations.AddField(
            model_name='datalog',
            name='session',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='exper.Session'),
        ),
        migrations.AddField(
            model_name='path',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='exper.Group'),
        ),
        migrations.AddField(
            model_name='path',
            name='session',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='exper.Session'),
        ),
        migrations.AddField(
            model_name='plan',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='exper.Group'),
        ),
        migrations.AddField(
            model_name='plan',
            name='session',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='exper.Session'),
        ),
        migrations.AddField(
            model_name='scenario',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='exper.Group'),
        ),
        migrations.AddField(
            model_name='scenario',
            name='session',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='exper.Session'),
        ),
        migrations.AddField(
            model_name='target',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='exper.Group'),
        ),
        migrations.AddField(
            model_name='target',
            name='session',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='exper.Session'),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='group',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='exper.Group'),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='session',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='exper.Session'),
        ),
        migrations.AddField(
            model_name='warehouse',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='exper.Group'),
        ),
        migrations.AddField(
            model_name='warehouse',
            name='session',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='exper.Session'),
        ),
        migrations.AddField(
            model_name='waypoint',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='exper.Group'),
        ),
        migrations.AddField(
            model_name='waypoint',
            name='session',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='exper.Session'),
        ),
        migrations.AlterField(
            model_name='datalog',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
