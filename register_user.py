#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys
sys.path.append('./libigetui')
sys.path.append('.')
sys.path.append('../../')
from bnb_grpc.user import config
from boto.dynamodb2.table import Table


tb_phone2uin = Table(config.table_name_phone2uin)
items = tb_phone2uin.scan()

for item in items:
    print (item['phone']).encode('utf8'), item['uin']
