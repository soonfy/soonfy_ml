#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'user id dist.'

# modules
import os

def write_file(users, filepath = r'./data/user_ids.txt'):
  if os.path.exists(os.path.split(filepath)[0]):
    pass
  else:
    os.makedirs(os.path.split(filepath)[0])
  user_str = ''.join(users)
  file_obj = open(filepath, 'w')
  file_obj.write(user_str)
  file_obj.close()

if __name__ == '__main__':
  print('>>> start hist douban ids ... \n')
  filer = open('./data/user_ids.txt', 'r+')
  lines = filer.readlines()
  print(len(lines))
  lines = set(lines)
  print(len(lines))
  write_file(lines, './data/id_dist.txt')
  filer.close()
