# Generated by Django 3.1.4 on 2020-12-19 02:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0007_auto_20201219_0159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job_details',
            name='recruter_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
