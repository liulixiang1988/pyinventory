# -*- coding:utf-8 -*-
__author__ = 'Administrator'

from django.forms import widgets
from rest_framework import serializers

from .models import Inventory, MaterialInventory


class InventorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Inventory
        fields = ('id', 'inventory_code', 'inventory_name', 'remark')

