#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/7/007 18:24
# @Author  : Woe
# @Site    : 
# @File    : mongodb.py
# @Software: PyCharm

from pymongo import MongoClient

from src.utils import singleton

@singleton
class PyMongoDb:
    _db = None
    MONGODB = {
        'MONGO_HOST': '127.0.0.1',
        'MONGO_PORT': '27017',
        'MONGO_USERNAME': '',
        'MONGO_PASSWORD': '',
        'DATABASE': 'Autologin'
    }

    def _client(self):
        self.mongo_uri = 'mongodb://{account}{host}:{port}/'.format(
            account='{username}:{password}@'.format(
                username=self.MONGODB['MONGO_USERNAME'],
                password=self.MONGODB['MONGO_PASSWORD']) if self.MONGODB['MONGO_USERNAME'] else '',
            host=self.MONGODB['MONGO_HOST'] if self.MONGODB['MONGO_HOST'] else 'localhost',
            port=self.MONGODB['MONGO_PORT'] if self.MONGODB['MONGO_PORT'] else 27017)
        return MongoClient(self.mongo_uri)

    @property
    def db(self):
        if self._db is None:
            self._db = self._client()[self.MONGODB['DATABASE']]

        return self._db