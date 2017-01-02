#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'crawl douban movie scores.'

__author__ = 'soonfy'

# modules
from urllib import request
from bs4 import BeautifulSoup
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

def crawl_score(url):
  """
  crawl movie score
  """
  body = request.urlopen(url).read().decode('utf-8')
  soup = BeautifulSoup(body, 'html.parser')
  rating_stars = [url]
  tag_spans = soup.findAll('span', class_='rating_per')
  for tag in tag_spans:
    rate = tag.string
    rating_stars.append(rate)
  tag_strong = soup.find('strong', class_='rating_num')
  if tag_strong:
    rating_num = tag_strong.string
    rating_stars.append(rating_num)
  return '\t'.join(rating_stars) + '\n'

def read_file():
  """
  read movie file
  """
  fd = open('./data/movies.txt')
  data = fd.readlines()
  return data

if __name__ == '__main__':
  filepath = './data/movie_scores.txt'
  head = 'url\trate5\trate4\trate3\trate2\trate1\trate\n'
  if file_ready(filepath):
    fd = open(filepath, 'a')
    fd.writelines(head)
    fd.close()
  data = read_file()
  for line in data:
    meta = line.split('\t')
    url = meta[1]
    if url.startswith('https'):
      score = crawl_score(url)
      fd = open(filepath, 'a')
      fd.writelines(score)
      fd.close()
      print('>> line over...')
  print('>> all lines over...')
