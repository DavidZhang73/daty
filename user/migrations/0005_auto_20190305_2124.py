# Generated by Django 2.1.7 on 2019-03-05 21:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('user', '0004_forgetpassword'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signinuserinfo',
            name='phone',
            field=models.CharField(blank=True, max_length=11, verbose_name='手机号'),
        ),
        migrations.AlterField(
            model_name='signinuserinfo',
            name='qq',
            field=models.CharField(blank=True, max_length=20, verbose_name='QQ'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(error_messages={'unique': 'Email已经被注册'}, max_length=254, unique=True,
                                    verbose_name='Email'),
        ),
    ]
