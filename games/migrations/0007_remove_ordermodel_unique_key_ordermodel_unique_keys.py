# Generated by Django 5.0.6 on 2024-06-07 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0006_alter_ordermodel_unique_key'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordermodel',
            name='unique_key',
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='unique_keys',
            field=models.JSONField(default=list),
        ),
    ]
