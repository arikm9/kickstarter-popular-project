# Generated by Django 2.1.3 on 2018-11-10 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('top_projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topprojects',
            name='date_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
