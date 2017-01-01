#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'crawl douban movie.'

__author__ = 'soonfy'

# modules
from urllib import request
import json

body = request.urlopen('https://movie.douban.com/j/search_subjects?type=movie&tag=热门&sort=time&page_limit=20&page_start=0').read().encode('utf-8')
obj = json.loads(body)
print(obj)
