# Generated by Django 2.2 on 2019-07-06 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0018_auto_20190620_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='accepted',
            field=models.BooleanField(default=True),
        ),
    ]
