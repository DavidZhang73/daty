# Generated by Django 2.1.7 on 2019-03-20 16:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('usergroup', '0002_auto_20190320_1329'),
    ]

    operations = [
        migrations.AddField(
            model_name='usergroup',
            name='creator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE,
                                    to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
