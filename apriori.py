#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# modules
from sklearn.neighbors import KNeighborsClassifier

from crawler import crawl_movie
from process import pre_data

def readLabels(filepath = r'./data/user_names.txt'):
  labels = []
  filer = open(filepath, 'r')
  label = filer.readline().strip()
  while label:
    label = label.split()[1]
    labels.append(label)
    label = filer.readline().strip()
  return labels

def knn(user_justify):
  cates, user_cates, names = pre_data.merge_category()
  data_traning = pre_data.count_category(cates, user_cates)[0:90]
  labels_traning = readLabels()[0:90]
  neigh = KNeighborsClassifier(n_neighbors = 15)
  neigh.fit(data_traning, labels_traning)
  data_justify = pre_data.count_category(cates, [user_justify])
  print(neigh.predict(data_justify))
  return neigh.predict_proba(data_justify)

if __name__ == '__main__':
  user_id = input('>>> what id u want to know:\n>>> ')
  user_cates = crawl_movie.get_movie(user_id)
  if not user_cates:
    print('>>> the id not see 100 movies...')
  else:
    # print(user_cates)
    crawl_movie.write_file(user_cates, r'./data/user/' + user_id + '.txt')
    justify = knn(user_cates)[0]
    print(justify)
    sex = None
    if justify[0] >= 0.5:
      print('>>> user %s has %s%% is a girl...' % (user_id, justify[0] * 100))
    else:
      print('>>> user %s has %s%% is a boy...' % (user_id, justify[1] * 100))
