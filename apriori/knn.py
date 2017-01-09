#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# modules
from sklearn import datasets

def test_knn():
  iris = datasets.load_iris()
  digits = datasets.load_digits()
  print(digits.data)
  print(digits.target)
