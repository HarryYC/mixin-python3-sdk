# -*- coding: utf-8 -*-
"""
Mixin API TEST for Python 3.x
env: python 3.x
code by lee.c
update at 2018.12.2
"""
from mixin_api import MIXIN_API
import mixin_config
import time

mixin_api = MIXIN_API(mixin_config)

print(mixin_api.verifyPin("896445"))
