# Generated by Django 5.0.1 on 2024-02-02 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_planes_plan'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='plan',
            name='updated',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
