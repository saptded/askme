# Generated by Django 3.2 on 2021-04-20 09:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('app', '0002_auto_20210419_2313'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='tags',
        ),
        migrations.AddField(
            model_name='question',
            name='tags',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE,
                                    to='app.tag'),
        ),
    ]
