# Generated by Django 4.1.4 on 2022-12-26 16:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tickets',
            name='status',
            field=models.CharField(blank=True, choices=[('Pending', 'Pending'), ('Opened', 'Opened'), ('Passed', 'Passed'), ('Failed', 'Failed'), ('Retest', 'Retest'), ('Closed', 'Closed')], default='Pending', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='tickets',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
