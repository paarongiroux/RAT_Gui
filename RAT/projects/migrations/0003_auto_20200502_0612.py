# Generated by Django 2.2 on 2020-05-02 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_project_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
