# Generated by Django 2.1.7 on 2019-06-02 10:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('usergroup', '0007_auto_20190320_1909'),
        ('utils', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid1, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='名称')),
                ('description', models.CharField(blank=True, max_length=300, null=True, verbose_name='要求')),
                ('start_datetime', models.DateTimeField(verbose_name='开始日期时间')),
                ('end_datetime', models.DateTimeField(verbose_name='结束日期时间')),
                ('create_datetime', models.DateTimeField(auto_now_add=True, verbose_name='创建日期时间')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL,
                                              verbose_name='创建人')),
                ('template_file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utils.UploadFile',
                                                    verbose_name='模板文件')),
                ('usergroup', models.ManyToManyField(to='usergroup.UserGroup', verbose_name='用户组')),
            ],
            options={
                'verbose_name': '文件集',
                'verbose_name_plural': '文件集',
            },
        ),
    ]