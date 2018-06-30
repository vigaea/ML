import numpy as np


def loadSimpData():
    dataMat = np.matrix([[1.,2.1],[2.,1.1],[1.3,1.],[1.,1.],[2.,1.]])
    classLabels = [1.0,1.0,-1.0,-1.0,1.0]
    return dataMat,classLabels

#对数据进行分类
def stumpClassify(dataMatrix,dimen,threshVal,threshIneq):
    retArray = np.ones((np.shape(dataMatrix)[0],1))  # 1矩阵，行数=矩阵行数。列数=1
    if threshIneq == 'lt':
        retArray[dataMatrix[:,dimen] <= threshVal] = -1.0
    else:
        retArray[dataMatrix[:,dimen] > threshVal] = -1.0
    return retArray
#找到最佳决策树
def buildStump(dataArr,classLabels,D):
    dataMatrix = np.mat(dataArr)
    labelMat = np.mat(classLabels).T  # 用mat函数转换为矩阵之后可以才进行一些线性代数的操作
    m,n = np.shape(dataMatrix)
    numSteps = 10.0
    bestStump = {}
    bestClasEst = np.mat(np.zeros((m,1)))
    minError = np.inf #最小错误率，开始初始化为无穷大
    for i in range(n):#遍历数据集所有特征
        rangeMin = dataMatrix[:,i].min()
        rangeMax = dataMatrix[:,i].max()
        stepSize = (rangeMax-rangeMin)/numSteps #考虑数据特征，计算步长
        for j in range(-1, int(numSteps) + 1):  #遍历不同步长时的情况
            for inequal in ['lt', 'gt']:  #大于/小于阈值 切换遍历
                threshVal = (rangeMin + float(j) * stepSize) #设置阈值
                predictedVals = stumpClassify(dataMatrix, i, threshVal,inequal) #分类预测
                errArr = np.mat(np.ones((m, 1)))#初始化全部为1（初始化为全部不相等）
                errArr[predictedVals == labelMat] = 0#预测与label相等则为0，否则为1
                # 分类器与adaBoost交互
                # 权重向量×错误向量=计算权重误差（加权错误率）
                weightedError = D.T * errArr
                # print("split:")
                if weightedError < minError:
                    minError = weightedError #保存当前最小的错误率
                    bestClasEst = predictedVals.copy() #预测类别
                    #保存该单层决策树
                    bestStump['dim'] = i
                    bestStump['thresh'] = threshVal
                    bestStump['ineq'] = inequal
    return bestStump, minError, bestClasEst #返回字典，错误率和类别估计

# if __name__ == '__main__':
#     dataMat, classLabels = loadSimpData()
#     D = np.mat(np.ones((5,1))/5)
#     bestStump, minError, bestClasEst = buildStump(dataMat,classLabels,D)