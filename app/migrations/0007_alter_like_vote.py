# Generated by Django 3.2 on 2021-04-20 12:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('app', '0006_auto_20210420_1050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='vote',
            field=models.SmallIntegerField(choices=[(1, 'Like')], verbose_name='Голос'),
        ),
    ]
