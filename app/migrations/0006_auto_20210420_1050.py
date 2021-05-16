# Generated by Django 3.2 on 2021-04-20 10:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('app', '0005_alter_question_tags'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Answer',
            new_name='Comment',
        ),
        migrations.AlterField(
            model_name='question',
            name='tags',
            field=models.ManyToManyField(to='app.Tag'),
        ),
    ]
