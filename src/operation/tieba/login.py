#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/8/008 21:15
# @Author  : Woe
# @Site    : 
# @File    : login.py
# @Software: PyCharm

from http.client import HTTPConnection
from src.utils import get_logger
logger = get_logger('Tieba_login')

def getCookieValue(cookies, cookieName):
    '''从cookies中获取指定cookie的值'''
    for cookie in cookies:
        if cookieName in cookie:
            index = cookie.index("=") + 1
            value = cookie[index:]
            return value

def getCookiesFromHeaders(headers):
    '''从http响应中获取所有cookie'''
    cookies = list()
    for header in headers:
        if "Set-Cookie" in header:
            cookie = header[1].split(";")[0]
            cookies.append(cookie)
    return cookies

def formatCookies(headers, cookies):
    '''保存cookies'''
    for cookie in cookies:
        headers["Cookie"] += cookie + ";"
    return headers

def tblogin(username, password):
    """

    :param username:
    :param password:
    :return: (header,cookies)
    """
    cookies = []
    headers = {
        "Connection": "keep-alive",
        "Cache-Control": "max-age=0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.107 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "gzip,deflate,sdch",
        "Accept-Language": "zh-CN,zh;q=0.8",
        "Cookie": "",
        "Host":"wappass.baidu.com"
    }
    body = f"username={username}&password={password}&submit=%E7%99%BB%E5%BD%95&quick_user=0&isphone=0&sp_login=waprate&uname_login=&loginmerge=1&vcodestr=&u=http%253A%252F%252Fwap.baidu.com%253Fuid%253D1392873796936_247&skin=default_v2&tpl=&ssid=&from=&uid=1392873796936_247&pu=&tn=&bdcm=3f7d51b436d12f2e83389b504fc2d56285356820&type=&bd_page_type="
    conn = HTTPConnection("wappass.baidu.com", 80)
    conn.request("POST", "/passport/login", body, headers)
    resp = conn.getresponse()
    cookies += getCookiesFromHeaders(resp.getheaders())

    headers = formatCookies(headers,cookies)
    logger.info('login success')
    return (headers,cookies)
if __name__ == '__main__':
    headers,cookies = tblogin("XXX","XXX")
    print(headers)
    print(cookies)