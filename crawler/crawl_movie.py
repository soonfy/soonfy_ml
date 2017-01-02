#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'crawl douban movie.'

__author__ = 'soonfy'

# modules
from urllib import request
from urllib import parse
import json
import os

def file_ready(filepath):
  """
  make filepath
  """
  try:
    if os.path.exists(os.path.split(filepath)[0]):
      if os.path.isfile(filepath):
        print('>> file exists...')
      else:
        print('>> file not exists...')
    else:
      os.makedirs(os.path.split(filepath)[0])
      print('>> make path success...')
    return True
  except Exception as e:
    print(e.reason)
    return False

def pick_tag(tag):
  """
  crawl tag movies 100 pages
  """
  filepath = './data/movies.txt'
  head = 'id\turl\trate\n'
  if file_ready(filepath):
    fd = open(filepath, 'a')
    fd.writelines(head)
    fd.close()
  page = 0
  while(True):
    page += 1
    url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=' + parse.quote(tag) + '&sort=time&page_limit=20&page_start=' + str(page * 20)
    body = request.urlopen(url).read().decode('utf-8')
    obj = json.loads(body)
    print(obj)
    arr = obj['subjects']
    length = len(arr)
    if length == 0:
      print('>> floop over, break...')
      break
    for subject in arr:
      temp = []
      temp.append(subject['id'])
      temp.append(subject['url'])
      temp.append(subject['rate'])
      sub_str = '\t'.join(temp) + '\n'
      fd = open(filepath, 'a')
      fd.writelines(sub_str)
      fd.close()
    print('>> the', page, 'page write success...')

if __name__ == '__main__':
  tag = input('>> input movie tag:\n')
  pick_tag(tag)
  print('>> all over...')
