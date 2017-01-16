#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# modules
# import tkinter
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

def run():
  data = [[0.8, 1.8], [1, 2.2], [1.5, 2.5], [2, 3], [1.8, 3.2], [2.5, 3], [1.5, 1.5], [1.5, 2], [2, 2],
  [2.5, 2], [3, 2.5], [2.2, 2.5]]
  labels = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]

  data = np.array(data)
  labels = np.array(labels)

  log_reg = linear_model.LogisticRegression(C=1e5)
  log_reg.fit(data, labels)

  print(log_reg.predict([[2.2, 3]]))
  print(log_reg.predict_log_proba([[2.2, 3]]))
  print(log_reg.predict_proba([[2.2, 3]]))

  print(log_reg.score([[2.2, 3]], [0]))

if __name__ == '__main__':
  run()
