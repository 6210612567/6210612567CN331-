# Generated by Django 3.2.6 on 2021-09-13 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_delete_register'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='remain',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='courses',
            name='seatquota',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
