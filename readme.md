# machine learning  

## apriori && pratice  
  1. machine learning  
    * [knn](knn)  
  2. scikit learn  
    * neighbors  

## KNN  

  1. k-近邻算法  
    * 优点：精度高，对异常值不敏感，无数据输入假定。  
    * 缺点：计算复杂度高，空间复杂度高。  
    * 适用数据范围：数值型，标称型。  
  2. 一般流程  
    * 收集数据：可以使用任何方法。  
    * 准备数据：距离计算所需要的数值，最好是结构化的数据格式。  
    * 分析数据：可以使用任何方法。  
    * 训练算法：此步骤不适用于k-近邻算法。  
    * 测试算法：计算错误率。  
    * 适用算法：首先需要输入样本数据和结构化的输出结果，然后运行k-近邻算法判定输入数据分别属于哪个分类，最后应用对计算出的分类执行后续的处理。  

## remark  

  1. import sklearn throw error "No module named _bz2"  
    * install libbz2-dev  
    * rebuild python  
  ```
  sudo apt-get install libbz2-dev
  make
  sudo make install
  ```

  2. import matplotlib throw error "No module named _tkinter"  
  ```
  sudo apt-get install python3-tk
  ```
