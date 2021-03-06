# Generated by Django 3.2 on 2021-04-08 06:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Student', '0002_auto_20210407_1520'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groupdata',
            name='group',
        ),
        migrations.AddField(
            model_name='studentdata',
            name='group',
            field=models.OneToOneField(default=2, on_delete=django.db.models.deletion.CASCADE, to='Student.groupdata'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
