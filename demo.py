#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'crawl douban movie scores.'

__author__ = 'soonfy'

# modules

from crawler import crawl_movie

print(crawl_movie.get_movie('orky'))
