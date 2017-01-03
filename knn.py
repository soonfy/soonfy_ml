from numpy import *
import operator
import matplotlib
import matplotlib.pyplot as plt

def createDataSet():
    group = array([[1.0, 0.9], [1.0, 1.0], [0, 0], [0, 0.1], [0.1, 0.1], [0.1, 0.2], [0.9, 0.8]])
    labels = ['A', 'A', 'B', 'B', 'B', 'B', 'A']
    return group, labels

def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances**0.5
    sortedDistIndicies = distances.argsort()
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]

group,lables=createDataSet()
print classify0([0.9, 0.9],group,lables,3)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(group[:,0], group[:,1])
plt.show( )
