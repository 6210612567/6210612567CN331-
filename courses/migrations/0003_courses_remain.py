# Generated by Django 3.2.6 on 2021-09-11 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20210911_1711'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='remain',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
