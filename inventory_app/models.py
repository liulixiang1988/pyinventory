# -*- coding:utf-8 -*-
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
# * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Inventory(models.Model):
    id = models.AutoField(primary_key=True)
    inventory_code = models.CharField(max_length=255, blank=True)
    inventory_name = models.CharField(max_length=255, blank=True)
    remark = models.CharField(max_length=255, blank=True)
    create_time = models.DateTimeField(blank=True, null=True)
    create_user_id = models.CharField(max_length=255, blank=True)
    create_user_name = models.CharField(max_length=255, blank=True)
    update_time = models.DateTimeField(blank=True, null=True)
    update_user_id = models.CharField(max_length=255, blank=True)
    update_user_name = models.CharField(max_length=255, blank=True)
    is_available = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inventory'
        verbose_name = '库存'
        verbose_name_plural = '库存'


class MaterialInventory(models.Model):
    id = models.AutoField(primary_key=True)
    item_code = models.CharField(max_length=255, blank=True)
    inventory_code = models.CharField(max_length=255, blank=True)
    create_time = models.DateTimeField(blank=True, null=True)
    create_user_id = models.CharField(max_length=255, blank=True)
    create_user_name = models.CharField(max_length=255, blank=True)
    update_time = models.DateTimeField(blank=True, null=True)
    update_user_id = models.CharField(max_length=255, blank=True)
    update_user_name = models.CharField(max_length=255, blank=True)
    is_available = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'material__inventory'
        verbose_name = '物料货位'
        verbose_name_plural = '物料货位'


class AnalysisResults(models.Model):
    id = models.AutoField(primary_key=True)
    sample_code = models.CharField(max_length=50, blank=True)
    sample_sub_id = models.CharField(max_length=50, blank=True)
    sample_date = models.DateTimeField(blank=True, null=True)
    sample_name = models.CharField(max_length=50, blank=True)
    sample_user_name = models.CharField(max_length=50, blank=True)
    sample_user_id = models.CharField(max_length=50, blank=True)
    mode = models.CharField(max_length=50, blank=True)
    burn = models.CharField(max_length=50, blank=True)
    element_name = models.CharField(max_length=50, blank=True)
    element_code = models.CharField(max_length=50, blank=True)
    element_value = models.CharField(max_length=50, blank=True)
    element_unit = models.CharField(max_length=20, blank=True)
    create_time = models.DateTimeField(blank=True, null=True)
    create_user_code = models.CharField(max_length=50, blank=True)
    create_user_name = models.CharField(max_length=50, blank=True)
    is_in_use = models.NullBooleanField()
    used_by = models.CharField(max_length=50, blank=True)
    remark = models.CharField(max_length=50, blank=True)
    attribute1 = models.CharField(max_length=50, blank=True)
    attribute2 = models.CharField(max_length=50, blank=True)
    attribute3 = models.CharField(max_length=50, blank=True)
    attribute4 = models.CharField(max_length=50, blank=True)
    attribute5 = models.CharField(max_length=50, blank=True)

    class Meta:
        managed = False
        db_table = 'tb_analysis_results'
        verbose_name = '分析结果'

