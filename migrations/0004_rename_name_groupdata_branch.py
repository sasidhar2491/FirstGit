# Generated by Django 3.2 on 2021-04-08 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0003_auto_20210408_1139'),
    ]

    operations = [
        migrations.RenameField(
            model_name='groupdata',
            old_name='name',
            new_name='branch',
        ),
    ]
