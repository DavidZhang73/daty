# Generated by Django 2.1.7 on 2019-03-03 16:22

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('user', '0002_signinuserinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signinuserinfo',
            name='id',
            field=models.CharField(default=uuid.uuid1, max_length=36, primary_key=True, serialize=False,
                                   verbose_name='ID'),
        ),
    ]