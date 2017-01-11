#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'crawl douban user movie.'

# modules
import time
import os

from urllib import request
from urllib.parse import urlencode

from bs4 import BeautifulSoup

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
  body = request.urlopen(collect)
  soup = BeautifulSoup(body, 'html.parser')
  next = get_next(soup)
  user_movies = parse_movie(soup, user_id)
  user_categorys = []
  index = 0
  for u_m in user_movies:
    index += 1
    url = u_m.split('\t')[1]
    try:
      body = request.urlopen(url)
    except Exception as e:
      if e.code == 404:
        print('>>> url %s not exist...' % url)
        index -= 1
        continue
      elif e.code == 403:
        print('>>> crawl too faster, sleep...')
        time.sleep(5)
        body = request.urlopen(url)
      else:
        print(e.reason)
        print('>>> wtf...')
    soup = BeautifulSoup(body, 'html.parser')
    categorys = get_category(soup)
    user_category = '\t'.join([user_id, url, categorys]) + '\n'
    user_categorys.append(user_category)
    print('>>> crawl the %s ...' % index)
  while(next):
    body = request.urlopen(next)
    soup = BeautifulSoup(body, 'html.parser')
    user_movies = parse_movie(soup, user_id)
    for u_m in user_movies:
      index += 1
      url = u_m.split('\t')[1]
      body = request.urlopen(url)
      soup = BeautifulSoup(body, 'html.parser')
      categorys = get_category(soup)
      user_category = '\t'.join([user_id, url, categorys]) + '\n'
      user_categorys.append(user_category)
      print('>>> crawl the %s ...' % index)
      if len(user_categorys) == amount:
        print('>>> user %s crawl success...' % user_id)
        return user_categorys
  print('>>> user %s collect movie less %s ...' % (user_id, amount))
  return None

if __name__ == '__main__':
  u_c = get_movie('67492098')
  write_file(u_c)
  print('>>> end... \n')
