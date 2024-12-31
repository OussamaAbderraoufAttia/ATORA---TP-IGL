# Generated by Django 5.1.4 on 2024-12-31 20:13

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medical_record', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='diagnostic',
            name='consultations',
            field=models.ManyToManyField(to='medical_record.consultation'),
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='date_creation',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='ordonnance',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='medical_record.ordonnance'),
        ),
    ]
