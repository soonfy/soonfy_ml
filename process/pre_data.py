#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'prepare and process data.'

__author__ = 'soonfy'

# modules
import os

def merge_category(filepath = r'./data/user_category.txt'):
  filer = open(filepath, 'r')
  index = 0
  all_category = []
  dist_category = []
  names = []
  name = temp = None
  while True:
    index += 1
    line = filer.readline().strip('\n')
    if len(line) == 0:
      all_category.append(temp)
      names.append(name)
      break
    metas = line.split('\t')
    if '' in metas:
      metas.remove('')
    dist_category += metas[2:]
    if metas[0] != name:
      if temp:
        all_category.append(temp)
        names.append(name)
      temp = []
      name = metas[0]
    else:
      temp += metas[2:]
    # print('>>> pre %s line data ...' % index)
  dist_category = set(dist_category)
  return dist_category, all_category, names

def count_category(cates, user_cates):
  data = []
  for user in user_cates:
    temp = []
    for cate in cates:
      temp.append(user.count(cate))
    data.append(temp)
  return data

def write_file(names, filepath = r'./data/user_names.txt'):
  if os.path.exists(os.path.split(filepath)[0]):
    pass
  else:
    os.makedirs(os.path.split(filepath)[0])
  user_str = '\n'.join(str(v) for v in names) + '\n'
  file_obj = open(filepath, 'w')
  file_obj.write(user_str)
  file_obj.close()

if __name__ == '__main__':
  cates, user_cates, names = merge_category(r'./data/user_category_test.txt')
  print(names)
  print(len(names))
  write_file(names, r'./data/user_names_test.txt')
  data = count_category(cates, user_cates)
  print(data)
  print(len(data))
