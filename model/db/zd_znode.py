#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# pylint: disable=invalid-name

from peewee import CharField
from peewee import IntegerField
from peewee import SQL

from model.db.base import ZKDASH_DB, EnumField


class ZdZnode(ZKDASH_DB.Model):

    """ZdZnode Model
    """

    id = IntegerField(primary_key=True, constraints=[SQL("AUTO_INCREMENT")])
    cluster_name = CharField(max_length=64, null=True)
    path = CharField(max_length=512, null=True)
    #type = EnumField(enum_value="'0', '1'", constraints=[SQL("DEFAULT '0'")])  # 节点属于普通节点还是文件节点，默认普通节点
    description = CharField(max_length=64, null=True)
    deleted = EnumField(enum_value="'0', '1'", constraints=[SQL("DEFAULT '0'")])

    class Meta(object):

        """表配置信息
        """
        db_table = "zd_znode"
