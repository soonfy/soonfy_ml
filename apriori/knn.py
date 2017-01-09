#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# modules
# from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier

def run():
  data = [[0.5, 0.5], [0.2, 0.3], [0.9, 0.1], [1.2, 0.8], [1.5, 0.6], [1.8, 0.3]]
  labels = [1, 1, 1, 2, 2, 2]
  neigh = KNeighborsClassifier(n_neighbors = 3)
  print(neigh.fit(data, labels))
  print(neigh.kneighbors([[0.9, 0.7], [1.6, 0.1]], 3, False))
  print(neigh.kneighbors_graph([[0.9, 0.7], [1.6, 0.1]], 3).toarray())
  print(neigh.predict([[0.9, 0.7], [1.6, 0.1]]))
  print(neigh.predict_proba([[0.9, 0.7], [1.6, 0.1]]))
  print(neigh.score([[0.9, 0.7], [1.6, 0.1]], [1, 1]))

# def test_knn():
#   iris = datasets.load_iris()
#   digits = datasets.load_digits()
#   print(digits.data)
#   print(digits.data[1])
#   print(len(digits.data[1]))
#   print(digits.target)
#   print(digits.target[1])
#   print(len(digits.target[1]))
