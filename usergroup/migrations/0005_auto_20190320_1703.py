# Generated by Django 2.1.7 on 2019-03-20 17:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('usergroup', '0004_auto_20190320_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usergroup',
            name='type',
            field=models.CharField(
                choices=[('NO NEED LOGIN', '不需要登陆'), ('ALREADY SIGNIN', '需要登陆已注册'), ('REQUIRE SIGNIN', '需要登陆未注册')],
                max_length=20, verbose_name='类型'),
        ),
    ]