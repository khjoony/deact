# Generated by Django 2.2.1 on 2019-07-30 03:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0005_auto_20190729_1457'),
    ]

    operations = [
        migrations.RenameField(
            model_name='kosdakinstance',
            old_name='ownner',
            new_name='owner',
        ),
        migrations.RenameField(
            model_name='kospiinstance',
            old_name='ownner',
            new_name='owner',
        ),
    ]
