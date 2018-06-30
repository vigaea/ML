import numpy as np
from Xgboost import adaboost

def loadSimpData():
    dataMat = np.matrix([[1.,2.1],[2.,1.1],[1.3,1.],[1.,1.],[2.,1.]])
    classLabels = [1.0,1.0,-1.0,-1.0,1.0]
    return dataMat,classLabels

if __name__ == '__main__':
    dataMat,labels = loadSimpData()
    array = np.ones((np.shape(dataMat)[0],1))
    m,n = np.shape(dataMat)
    print(np.mat(dataMat))
    print(m,n)
    print(array)



