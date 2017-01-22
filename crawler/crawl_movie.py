#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'crawl douban user movie.'

__author__ = 'soonfy'

# modules
import time
import os
import re

from urllib import request
from urllib.parse import urlencode

from bs4 import BeautifulSoup

# from crawler import spider
import spider

def log(s):
  index = 0
  while index * 60 < s:
    index += 1
    time.sleep(60)
    print('>>> %s min ...' % index)

def get_next(soup):
  """
  get next url from douban user-movie html  
  @param soup  
  @return next_url
  """
  tag_span = soup.find('span', class_='next')
  tag_a = None
  if tag_span:
    tag_a = tag_span.find('a')
  url = None
  if tag_a:
    url = tag_a['href']
  return url

def parse_movie(soup, user_id):
  """
  get movie uri
  """
  tag_divs = soup.find_all('div', class_='item')
  user_movies = []
  for tag in tag_divs:
    tag_a = tag.find('li', class_='title').find('a')
    movie_url = tag_a['href']
    user_movie = '%s\t%s' % (user_id, movie_url)
    user_movies.append(user_movie)
  return user_movies

def get_category(soup):
  """
  get movie category
  """
  tag_spans = soup.select('span[property="v:genre"]')
  categorys = []
  for span in tag_spans:
    category = span.string
    categorys.append(category)
  return '\t'.join(categorys)

def write_file(user_category, filepath = r'./data/user_category.txt'):
  if os.path.exists(os.path.split(filepath)[0]):
    pass
  else:
    os.makedirs(os.path.split(filepath)[0])
  user_str = '\n'.join(user_category) + '\n'
  file_obj = open(filepath, 'a')
  file_obj.write(user_str)
  file_obj.close()

def get_movie(user_id, amount = 100):
  collect = 'https://movie.douban.com/people/%s/collect' % user_id
  body = None
  try:
    opener = spider.create_spider()
    body = opener.open(collect)
  except Exception as e:
    if e.code and e.code == 404:
      print('>>> url %s not exist...' % collect)
      return None
    elif e.code and e.code == 403:
      print('>>> crawl too faster, sleep 30m...')
      log(60 * 30)
      opener = spider.create_spider()
      body = opener.open(collect)
    else:
      print(e.reason)
      print('>>> wtf...')
  soup = BeautifulSoup(body, 'html.parser')
  tag_h = soup.h1
  if tag_h:
    user_collect = tag_h.string
    # print('>>> ', user_collect)
    m = re.search(r'看过的电影\((\d*)\)', user_collect)
    if m and int(m.group(1)) >= amount:
      # print('>>> ', m.group(1))
      pass
    else:
      print('>>> user %s collect movie less %s ...' % (user_id, amount))
      return None
  else:
    print('>>> user %s collect movie less %s ...' % (user_id, amount))
    return None
  next = get_next(soup)
  user_movies = parse_movie(soup, user_id)
  user_categorys = []
  index = 0
  for u_m in user_movies:
    index += 1
    url = u_m.split('\t')[1]
    try:
      opener = spider.create_spider()
      body = opener.open(url)
    except Exception as e:
      print(e)
      if e.code and e.code == 404:
        print('>>> url %s not exist...' % url)
        index -= 1
        continue
      elif e.code and e.code == 403:
        print('>>> crawl too faster, sleep 30m...')
        log(60 * 30)
        opener = spider.create_spider()
        body = opener.open(url)
      else:
        print(e.reason)
        print('>>> wtf...')
    soup = BeautifulSoup(body, 'html.parser')
    categorys = get_category(soup)
    user_category = '\t'.join([user_id, url, categorys])
    user_categorys.append(user_category)
    print('>>> crawl the %s movie ...' % index)
    if len(user_categorys) >= amount:
      # print('>>> user %s crawl success...' % user_id)
      return user_categorys
  while(next):
    try:
      opener = spider.create_spider()
      body = opener.open(next)
    except Exception as e:
      if e.code and e.code == 404:
        print('>>> url %s not exist...' % next)
        index -= 1
        continue
      elif e.code and e.code == 403:
        print('>>> crawl too faster, sleep 30m...')
        log(60 * 30)
        opener = spider.create_spider()
        body = opener.open(next)
      else:
        print(e.reason)
        print('>>> wtf...')
    soup = BeautifulSoup(body, 'html.parser')
    next = get_next(soup)
    user_movies = parse_movie(soup, user_id)
    for u_m in user_movies:
      index += 1
      url = u_m.split('\t')[1]
      try:
        opener = spider.create_spider()
        body = opener.open(url)
      except Exception as e:
        if e.code and e.code == 404:
          print('>>> url %s not exist...' % url)
          index -= 1
          continue
        elif e.code and e.code == 403:
          print('>>> crawl too faster, sleep 30m...')
          log(60 * 30)
          opener = spider.create_spider()
          body = opener.open(url)
        else:
          print(e.reason)
          print('>>> wtf...')
      soup = BeautifulSoup(body, 'html.parser')
      categorys = get_category(soup)
      user_category = '\t'.join([user_id, url, categorys])
      user_categorys.append(user_category)
      print('>>> crawl the %s movie ...' % index)
      if len(user_categorys) >= amount:
        print('>>> user %s crawl success...' % user_id)
        return user_categorys
  print('>>> user %s collect movie less %s ...' % (user_id, amount))
  return None

if __name__ == '__main__':
  amount = input('>>> crawl user amount... \n>>> ')
  filer = open(r'./data/id_dist.txt', 'r')
  index = 0
  line = 0
  while index < int(amount):
    index += 1
    line += 1
    user_id = filer.readline().strip('\n')
    print('>>> read the %s line ...' % (line))
    # restart
    # if line < 343:
    if line < 1058:
      index -= 1
      continue
    if len(user_id) > 0:
      print('>>> crawl the %s user -> %s ...' % (index, user_id))
      u_c = None
      try:
        u_c = get_movie(user_id)
      except Exception as e:
        u_c = get_movie(user_id)
      if u_c:
        write_file(u_c, r'./data/user_category.txt')
      else:
        index -= 1
  print('>>> end... \n')
