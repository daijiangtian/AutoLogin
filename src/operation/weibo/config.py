#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/7/007 19:20
# @Author  : Woe
# @Site    : 
# @File    : config.py
# @Software: PyCharm


# 发送设置
TIME_SLOG = 30 * 60                 # 发送微博的时间间隔 (秒)
MAX_IMAGES = 0                      # 允许上传图片的最大数量。如果设置为0，则不上传图片。
ADD_WATERMARK = False               # 是否添加图片水印，为True时，应设置以下两项
WATERMARK_NIKE = "@微博"             # 水印名称
WATERMARK_URL = "weibo.com"         # 水印链接

# 系统设置
WBCLIENT = 'ssologin.js(v1.4.18)'

USER_AGENT = (
      'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.11 (KHTML, like Gecko) '
      'Chrome/20.0.1132.57 Safari/536.11'
)

