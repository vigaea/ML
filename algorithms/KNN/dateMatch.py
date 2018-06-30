from numpy import *
import numpy as np
import operator
import matplotlib.pyplot as plt

def classify(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inX, (dataSetSize,1)) - dataSet  # tile复制数组，个数为dataSetSize。
    seqDiffmat = diffMat ** 2
    seqDis = seqDiffmat.sum(axis=1)  # 按行相加
    distances = seqDis ** 0.5
    sortedDisIndicies = distances.argsort()  # argsort返回数值从小到大的索引值
    classCount = {}
    for i in range(k):
        voteLabel = labels[sortedDisIndicies[i]]  # 根据排序结果，返回距离最近的前k个标签
        classCount[voteLabel] = classCount.get(voteLabel,0) + 1  # 统计标签次数
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)  # key按行排序
    return sortedClassCount[0][0]  # 找出频率最高的，属于哪个label


# 文件转矩阵
def file2Mat(filename):
    file = open(filename)
    arrayLines = file.readlines()
    numLines = len(arrayLines)  # 读取文件行数
    returnMat = np.zeros((numLines, 3))  # 创建行数=文件行数，烈属=3 的零矩阵
    classLabels = []
    index = 0
    for line in arrayLines:
        line = line.strip()  # 截取所有回车字符
        line = line.split('\t')
        returnMat[index,:] = line[0:3]  # 将文件前3列写入矩阵，最后一列写入label
        classLabels.append(int(line[-1]))
        index += 1
    return returnMat,classLabels

# 矩阵归一化    new = (old-min) / (max-min)
def norm(dataSet):
    min = dataSet.min(0)  # 按列找出最小值，返回1x3矩阵
    max = dataSet.max(0)
    ranges = max - min
    r=dataSet.shape[0]
    normMat = np.zeros(shape(dataSet))
    normMat = dataSet - np.tile(min, (r,1))
    normMat = normMat / np.tile(ranges, (r,1))
    return normMat, ranges, min


if __name__ == '__main__':
# def datingTest():
    datingMat, datingLabels = file2Mat("D:\DATA\ML\datingTestSet2.txt")
    # print(datingMat.shape[0])
    # print(datingMat.shape[1])
    # # print(datingMat.min(0))
    # # print(datingMat.max(0))
    # print(datingMat[0:10], datingLabels[0:10])
    #
    # normMat, ranges, min = norm(datingMat)
    # print(normMat[0:3], ranges, min)

    # # trainingSet部分可视化
    # fig = plt.figure()
    # ax = fig.add_subplot(111)
    # ax.scatter(datingMat[:,1], datingMat[:,2], 15.0 * np.array(datingLabels), 15.0 * np.array(datingLabels))
    # plt.show()

    # 测试的准确率
    normMat, ranges, min = norm(datingMat)
    testRatio = 0.10
    errorCount = 0.0
    r = normMat.shape[0]
    numTest = int(r * testRatio)
    for i in range(numTest):
        classifyResult = classify(normMat[i,:], normMat[numTest:r,:], datingLabels[numTest:r], 3)
        print('classifying with: %d, real class is: %d' % (classifyResult, datingLabels[i]))
        if(classifyResult != datingLabels[i]):
            errorCount += 1.0
    errorRate = errorCount / (float(numTest))
    accu = 1 - errorRate
    print('accuracy is: %f, error rate is: %f' % (accu, errorRate))

# def classifyPerson():
    resultList=['not at all','in small doses','in large doses']
    percentTats=float(input("percentage of time spent playing video games?"))
    ffMiles=float(input("frequent flier miles earned per year?"))
    iceCream=float(input("liters of ice cream consumed per year?"))
    inArr=array([ffMiles,percentTats,iceCream])
    classifierResult=classify((inArr-min)/ranges, normMat, datingLabels, 3)
    print("You will probably like this person:", resultList[classifierResult-1])