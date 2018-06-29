# Generated by Django 2.0.3 on 2018-06-25 11:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reports', '0003_auto_20180625_1025'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='assigned_to',
            field=models.ManyToManyField(related_name='report_assigned_to', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='answer',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='report',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='report_created_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
