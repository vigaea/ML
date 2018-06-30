import numpy as np
import operator

def createDataset():
    group = np.array([[1.0, 1.1],[1.0,1.1],[0.0,0.0],[0.0,0.1]])
    labels = ['A', 'B', 'C', 'D']
    return group,labels

def classify(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = np.tile(inX, (dataSetSize,1)) - dataSet  # tile复制数组，个数为dataSetSize。
    seqDiffmat = diffMat ** 2
    seqDis = seqDiffmat.sum(axis=1)  # 按行相加
    distances = seqDis ** 0.5
    sortedDisIndicies = distances.argsort()  # argsort返回数值从小到大的索引值
    print(sortedDisIndicies)
    classCount = {}
    for i in range(k):
        voteLabel = labels[sortedDisIndicies[i]]  # 根据排序结果，返回距离最近的前k个标签
        classCount[voteLabel] = classCount.get(voteLabel,0) + 1  # 统计标签次数
        print(classCount)
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)  # key按行排序
    print(sortedClassCount)
    return sortedClassCount[0][0]  # 找出频率最高的，属于哪个label

if __name__ == '__main__':  # __name__ 是当前模块名，当模块被直接运行时，以下代码块将被运行，当模块是被导入时，代码块不被运行。
    group, labels = createDataset()
    test = classify([0.6,0.6], group, labels, 3)
    print(test)

