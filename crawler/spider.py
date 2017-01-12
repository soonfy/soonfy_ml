#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'douban spider: nologin.'

__author__ = 'soonfy'

# modules
import random

from urllib import request
from http import cookiejar

def read_ua(filepath = r'./data/ua.txt'):
  """
  read ua from file  
  @param filepath  
  @return ua  
  """
  file_obj = open(filepath, 'r')
  ua_str = file_obj.read()
  file_obj.close()
  uas = ua_str.split('\n')
  ua = random.choice(uas)
  print(ua)
  return ua

def create_spider():
  """
  nologin douban spider  
  @return opener  
  """
  header = {
    'User-Agent': read_ua(),
    'Referer': 'https://www.douban.com/',
    'Host': 'www.douban.com',
    'Origin': 'https://www.douban.com'
  }
  headers = []
  for key, value in header.items():
    elem = (key, value)
    headers.append(elem)
  cj = cookiejar.CookieJar()
  handler = request.HTTPCookieProcessor(cj)
  opener = request.build_opener(handler)
  request.install_opener(opener)
  opener.addheaders = headers
  return opener
