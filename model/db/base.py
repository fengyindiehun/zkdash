#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

from peewee import Field

from lib.db.database import Database
from conf.settings import DATABASE

# 后台管理数据库
ZKDASH_DB = Database(**DATABASE)


class EnumField(Field):
    """自定义枚举类型字段, peewee中不提供枚举类型
    """
    db_field = 'enum'

    def __init__(self, enum_value=None, *args, **kwargs):
        """枚举初始化
        """
        self.enum_value = enum_value
        super(EnumField, self).__init__(*args, **kwargs)

    def get_modifiers(self):
        """使用传递的枚举值
        """
        return self.enum_value and [self.enum_value] or None
