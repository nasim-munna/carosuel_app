# Generated by Django 3.2.7 on 2021-11-13 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nasimit', '0003_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_url',
            field=models.URLField(null=True),
        ),
    ]
