#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/7/007 19:40
# @Author  : Woe
# @Site    : 
# @File    : login.py
# @Software: PyCharm

from src.operation.weibo.login import wblogin
from src.operation.weibo.sender import WeiboSender
from src.operation.weibo.message import WeiboMessage
if __name__ == '__main__':
    (http, uid) = wblogin(username='XXX',password='XXX')
    print(uid)

    sender = WeiboSender(session=http,uid=uid)

    message = WeiboMessage(text='小柴柴和橘千代')

    sender.send_weibo(message)