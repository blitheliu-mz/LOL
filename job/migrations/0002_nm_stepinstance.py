# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-09-11 21:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nm_StepInstance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stepId', models.IntegerField(null=True, verbose_name='\u6267\u884c\u6b65\u9aa4id')),
                ('appId', models.IntegerField(null=True, verbose_name='\u4e1a\u52a1id')),
                ('name', models.CharField(max_length=255, null=True, verbose_name='\u811a\u672c\u540d\u79f0')),
                ('type', models.IntegerField(null=True, verbose_name='\u6b65\u9aa4\u7c7b\u578b')),
                ('ord', models.IntegerField(null=True, verbose_name='\u5c0f\u6b65\u9aa4\u6267\u884c\u7684\u6b21\u5e8f')),
                ('blockOrd', models.IntegerField(null=True, verbose_name='\u5757\u6b21\u5e8f')),
                ('blockName', models.CharField(max_length=255, null=True, verbose_name='\u5757\u540d\u79f0')),
                ('account', models.CharField(max_length=255, null=True, verbose_name='\u76ee\u6807\u673a\u5668\u7684\u6267\u884c\u8d26\u6237\u540d')),
                ('badIpList', models.CharField(max_length=255, null=True, verbose_name='Agent\u5f02\u5e38\u7684ip\u5217\u8868')),
                ('scriptContent', models.TextField(null=True, verbose_name='\u6267\u884c\u811a\u672c\u7684\u5185\u5bb9')),
                ('scriptType', models.IntegerField(null=True, verbose_name='\u6267\u884c\u811a\u672c\u7684\u7c7b\u578b')),
                ('scriptParam', models.CharField(default=True, max_length=255, null=True, verbose_name='\u6267\u884c\u811a\u672c\u7684\u53c2\u6570')),
                ('scriptTimeout', models.IntegerField(null=True, verbose_name='\u6267\u884c\u811a\u672c\u7684\u8d85\u65f6\u65f6\u95f4')),
                ('fileSource', models.CharField(max_length=255, null=True, verbose_name='\u6587\u4ef6\u4f20\u8f93\u7684\u6e90\u6587\u4ef6')),
                ('fileSpeedLimit', models.IntegerField(null=True, verbose_name='\u4f20\u8f93\u6587\u4ef6\u7684\u9650\u901f')),
                ('text', models.CharField(max_length=255, null=True, verbose_name='\u6587\u672c\u901a\u77e5')),
                ('operator', models.CharField(max_length=255, null=True, verbose_name='\u6267\u884c\u4eba')),
                ('status', models.IntegerField(default=1, null=True, verbose_name='\u72b6\u6001')),
                ('retryCount', models.IntegerField(default=1, null=True, verbose_name='\u91cd\u8bd5\u6b21\u6570')),
                ('startTime', models.DateTimeField(null=True, verbose_name='\u5f00\u59cb\u65f6\u95f4')),
                ('endTime', models.DateTimeField(null=True, verbose_name='\u7ed3\u675f\u65f6\u95f4')),
                ('totalTime', models.FloatField(default=False, max_length=11, null=True, verbose_name='\u603b\u8017\u65f6')),
                ('totalIPNum', models.IntegerField(null=True, verbose_name='\u603bip\u6570\u91cf')),
                ('badIPNum', models.IntegerField(null=True, verbose_name='\u6ca1\u6709agent')),
                ('runIPNum', models.IntegerField(null=True, verbose_name='\u6709agent')),
                ('failIPNum', models.IntegerField(null=True, verbose_name='\u5931\u8d25ip\u6570\u91cf')),
                ('successIPNum', models.IntegerField(null=True, verbose_name='\u6210\u529fip\u6570\u91cf')),
                ('createTime', models.DateTimeField(auto_now_add=True, null=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('isPause', models.IntegerField(default=0, null=True, verbose_name='\u662f\u5426\u9700\u8981\u6682\u505c')),
                ('companyId', models.IntegerField(default=0, null=True, verbose_name='\u5f00\u53d1\u5546id')),
                ('isUseCCFileParam', models.IntegerField(default=0, null=True, verbose_name='')),
                ('taskInstanceId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nm_instance_set', to='job.Nm_Instance')),
            ],
            options={
                'db_table': 'nm_stepInstance',
            },
        ),
    ]