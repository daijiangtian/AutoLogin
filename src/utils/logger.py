#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/7/007 19:21
# @Author  : Woe
# @Site    : 
# @File    : logger.py
# @Software: PyCharm

import logging

def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    # log format
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger