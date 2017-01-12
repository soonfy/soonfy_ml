#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'crawl user relations.'

# modules
import time
import os
import re
import sys

from urllib import request
from urllib.parse import urlencode
from http import cookiejar

from bs4 import BeautifulSoup

def spider_login():
  """
  login douban spider  
  @return opener  
  """
  url_login = 'https://www.douban.com/accounts/login'
  param = {
    "source": 'None',
    "redir": 'https://www.douban.com/people/67492098/contacts',
    "form_email": 'soonfy@163.com',
    "form_password": 'soonfy163',
    "login": '登录',
    # "captcha-id": 'TWYNLemDPICzffLYfv7v2XQn:en',
    # "captcha-solution": 'again'
  }
  data = urlencode(param).encode('utf-8')
  headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Referer': 'https://www.douban.com/people/67492098/contacts',
    'Host': 'www.douban.com',
    'Origin': 'https://www.douban.com'
  }
  req = request.Request(url_login, data, headers)
  filename = os.path.abspath(r'./data/cookie.txt')
  FileCookieJar= cookiejar.MozillaCookieJar(filename)
  FileCookieJar.save()
  handler = request.HTTPCookieProcessor(FileCookieJar)
  opener = request.build_opener(handler)
  request.install_opener(opener)
  res = request.urlopen(req)
  body = res.read().decode('utf-8')
  FileCookieJar.save()
  print(body)
  return opener

def parse_users(body):
  soup = BeautifulSoup(body, 'html.parser')
  tag_dls = soup.find_all('dl')
  user_ids = []
  for tag in tag_dls:
    tag_a = tag.dd.a
    user_url = tag_a['href']
    m = re.search(r'/people/(\w+)/', user_url)
    if m:
      user_ids.append(m.group(1))
  return user_ids

def write_file(users, filepath = r'./data/user_ids.txt'):
  if os.path.exists(os.path.split(filepath)[0]):
    pass
  else:
    os.makedirs(os.path.split(filepath)[0])
  user_str = '\n'.join(users) + '\n'
  file_obj = open(filepath, 'a')
  file_obj.write(user_str)
  file_obj.close()

def get_relations(opener, user_id):
  user_ids = []
  contacts = 'https://www.douban.com/people/%s/contacts' % user_id
  rev_contacts = 'https://www.douban.com/people/%s/rev_contacts' % user_id

  time.sleep(2)
  body = opener.open(contacts)
  con_ids = parse_users(body)
  write_file(con_ids)

  time.sleep(1)
  body = opener.open(rev_contacts)
  rev_ids = parse_users(body)
  write_file(rev_ids)
  
  user_ids = con_ids + rev_ids
  return user_ids

if __name__ == '__main__':
  write_file([], r'./data/user_ids.txt')
  opener = spider_login()
  login = input('>>> login ? y or n ... \n>>> ')
  amount = input('>>> crawl user amount... \n>>> ')
  amount = int(amount)
  if login == 'y':
    user_id = input('>>> start douban user id, ex 67492098 ... \n>>> ')
    write_file([user_id])
    user_ids = get_relations(opener, user_id)
    index = 0
    count = 0
    for id in user_ids:
      index += 1
      print('>>> start crawl douban user %s ...' % id)
      new_ids = get_relations(opener, id)
      nums = len(new_ids)
      count += nums
      print('>>> this user relations length %s ...' % nums)
      print('>>> all users length %s ...' % count)
      user_ids = user_ids + new_ids
      print('>>> already crawl %s user ...' % index)
      if count >= amount:
        print('>>> already crawl amount %s user ...' % count)
        print('>>> end ...')
        sys.exit()
  else:
    print('>>> no login, exit ...')
