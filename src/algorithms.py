import numpy as np
import pandas as pd
from flask import jsonify
import math
from scipy.spatial import KDTree
from numpy import random
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.mixture import GaussianMixture
from pysal.explore.esda.getisord import G_Local

class visitlist:
    def __init__(self, count=0):
        self.unvisitedlist=[i for i in range(count)]
        self.visitedlist=list()
        self.unvisitednum=count

    def visit(self, pointId):
        self.visitedlist.append(pointId)
        self.unvisitedlist.remove(pointId)
        self.unvisitednum -= 1

def dbscan(dataSet, eps, minPts):
    nPoints = dataSet.shape[0]
    vPoints = visitlist(count=nPoints)
    # 初始化簇标记列表C，簇标记为 k
    k = -1
    C = [-1 for i in range(nPoints)]
    # 构建KD-Tree，并生成所有距离<=eps的点集合
    kd = KDTree(dataSet)
    while(vPoints.unvisitednum>0):
        p = random.choice(vPoints.unvisitedlist)
        vPoints.visit(p)
        N = kd.query_ball_point(dataSet[p], eps)
        if len(N) >= minPts:
            k += 1
            C[p] = k
            for p1 in N:
                if p1 in vPoints.unvisitedlist:
                    vPoints.visit(p1)
                    M = kd.query_ball_point(dataSet[p1], eps)
                    if len(M) >= minPts:
                        for i in M:
                            if i not in N:
                                N.append(i)
                    if C[p1] == -1:
                        C[p1] = k
        else:
            C[p] = -1
    return C


def DecisionTree(x_train, y_train, x_test):
    clf = DecisionTreeClassifier()
    clf.fit(x_train, y_train)
    y_pred = clf.predict(x_test)
    return y_pred

def GaussianMixture(Xs):
    gmm = GaussianMixture(n_components=3).fit(Xs)
    labels = gmm.predict(Xs)
    return labels

def rand_center(dataSet, k):
    """构建一个包含K个随机质心的集合"""
    n = np.shape(dataSet)[1]  # 获取样本特征值
    centroids = np.array(np.zeros((k, n)))  # 每个质心有n个坐标值，总共要k个质心
    if not dataSet.any():
        return centroids
    # 遍历特征值
    for j in range(n):
        minJ = np.min(dataSet[:, j])
        rangeJ = float(max(dataSet[:, j]) - minJ)
        if rangeJ:
            centroids[:, j] = (minJ + rangeJ * np.random.rand(k, 1)).squeeze()
    return centroids  # 返回质心

def distance_eucl(vec1, vec2):
    """计算欧氏距离"""
    return np.sqrt(np.sum(np.power(vec1 - vec2, 2)))

def distance_cos(vec1, vec2):
    """余弦距离"""
    return np.sum(vec1.dot(vec2.T))



def k_means_asc(dataSet, k, distMeas, creatCent):
    m = np.shape(dataSet)[0]  # 行数
    # 建立簇分配结果矩阵，第一列存放该数据所属中心点，第二列是该数据到中心点的距离
    clusterAssment = np.array(np.zeros((m, 2)))
    centroids = eval(creatCent)(dataSet, k)  # 质心，即聚类点
    # 用来判定聚类是否收敛
    clusterChanged = True
    n = 0;
    while clusterChanged:
        clusterChanged = False
        for i in range(m):  # 把每一个数据划分到离他最近的中心点
            minDist = np.inf  # 无穷大
            minIndex = -1 # 初始化
            vec2 = dataSet[i, :]
            for j in range(k):
                # 计算各点与新的聚类中心的距离
                vec1 = centroids[j, :]
                distJI = eval(distMeas)(vec1, vec2)
                if minDist > distJI:
                    # 如果第i个数据点到第j中心点更近，则将i归属为j
                    minDist = distJI
                    minIndex = j
            # 如果分配发生变化，则需要继续迭代
            if clusterAssment[i, 0] != minIndex:
                clusterChanged = True
                # 并将第i个数据点的分配情况存入字典
                clusterAssment[i, :] = minIndex, minDist ** 2
        # print(centroids)
        for cent in range(k):  # 重新计算中心点
            # 取第一列等于cent的所有列
            ptsInClust = dataSet[np.nonzero(clusterAssment[:, 0] == cent)[0]]
            # 算出这些数据的中心点
            if not ptsInClust.any():
                centroids[cent, :] = 0
            else:
                centroids[cent, :] = np.mean(ptsInClust, axis=0)
    return centroids, clusterAssment

def k_means_desc(dataSet, k, distMeas, creatCent):
    m = np.shape(dataSet)[0]  # 行数
    # 建立簇分配结果矩阵，第一列存放该数据所属中心点，第二列是该数据到中心点的距离
    clusterAssment = np.array(np.zeros((m, 2)))
    centroids = eval(creatCent)(dataSet, k)  # 质心，即聚类点
    # 用来判定聚类是否收敛
    clusterChanged = True
    n = 0;
    while clusterChanged:
        clusterChanged = False
        for i in range(m):  # 把每一个数据划分到离他最近的中心点
            minDist = 0  # 无穷大
            minIndex = -1 # 初始化
            vec2 = dataSet[i, :]
            for j in range(k):
                # 计算各点与新的聚类中心的距离
                vec1 = centroids[j, :]
                distJI = eval(distMeas)(vec1, vec2)
                if minDist < distJI:
                    # 如果第i个数据点到第j中心点更近，则将i归属为j
                    minDist = distJI
                    minIndex = j
            # 如果分配发生变化，则需要继续迭代
            if clusterAssment[i, 0] != minIndex:
                clusterChanged = True
                # 并将第i个数据点的分配情况存入字典
                clusterAssment[i, :] = minIndex, minDist ** 2
        # print(centroids)
        for cent in range(k):  # 重新计算中心点
            # 取第一列等于cent的所有列
            ptsInClust = dataSet[np.nonzero(clusterAssment[:, 0] == cent)[0]]
            # 算出这些数据的中心点
            if not ptsInClust.any():
                centroids[cent, :] = 0
            else:
                centroids[cent, :] = np.mean(ptsInClust, axis=0)
    return centroids, clusterAssment

def Kmeans(dataSet, k, distMeas, creatCent='rand_center'):
    if distMeas != 'distance_cos':
        centroids, clusterAssment = k_means_asc(dataSet, k, distMeas, creatCent)
    else:
        centroids, clusterAssment = k_means_desc(dataSet, k, distMeas, creatCent)
    return centroids, clusterAssment

def KNN(x_train, y_train, x_test, k):
    x_train = np.array(x_train)
    y_train = np.array(y_train)
    x_test = np.array(x_test)
    y_pred = []
    for i in range(len(x_test)):
        distances = np.sqrt(np.sum(np.square(x_train - x_test[i]), axis=1))
        nearest = np.argsort(distances)
        topK_y = y_train[nearest][:k]
        y_pred.append(np.argmax(np.bincount(topK_y.astype('int'))))
    return y_pred

def DecisionTreeClassification(x_train, y_train, x_test, criterion, splitter):
    clf = DecisionTreeClassifier(criterion=criterion, splitter=splitter)
    clf.fit(x_train, y_train)
    y_pred = clf.predict(x_test)
    return y_pred

def LinearRegression(x_train, y_train, x_test):
    x_train = np.array(x_train)
    y_train = np.array(y_train)
    x_train = np.insert(x_train, 0, 1, axis=1)
    xTx = x_train.T.dot(x_train)
    ws = np.linalg.inv(xTx).dot(x_train.T).dot(y_train)
    return ws

def LogisticRegression(x_train, y_train, x_test):
    clf = LogisticRegression()

    # 使用训练集训练模型
    clf.fit(x_train, y_train)

    y_pred = clf.predict(x_test)
    return y_pred

from pysal.lib import weights
def LocalG(y, gdf):
    '''
    y: array
    gdf: geodataframe
    '''
    w = weights.Queen.from_dataframe(gdf)
    lg = G_Local(y, w)
    return lg.Gs

from pysal.explore.esda.moran import Moran_Local

def LocalMoransI(y, gdf):
    '''
    y: array
    gdf: geodataframe
    '''
    w = weights.Queen.from_dataframe(gdf)
    mi = Moran_Local(y, w)
    return mi.Is


from pysal.explore.esda.moran import Moran

def MoransI(y, gdf):
    '''
    y: array
    gdf: geodataframe
    '''
    w = weights.Queen.from_dataframe(gdf)
    mi = Moran(y, w)
    return mi.I

from sklearn.ensemble import RandomForestRegressor

def RandomForestRegression(x_train, y_train, x_test, criterion):
    '''
    x_train: 训练数据
    y_train: 训练数据的目标值
    x_test: 测试数据
    '''
    reg = RandomForestRegressor(criterion=criterion)
    reg.fit(x_train, y_train)
    y_pred = reg.predict(x_test)
    return y_pred

from sklearn.linear_model import Ridge

def RidgeRegression(x_train, y_train, x_test):
    '''
    x_train: 训练数据
    y_train: 训练数据的目标值
    x_test: 测试数据
    '''
    reg = Ridge()
    reg.fit(x_train, y_train)
    y_pred = reg.predict(x_test)
    return y_pred

from sklearn.svm import SVC, SVR

def SVMClassification(x_train, y_train, x_test, C, kernelfunc):
    '''
    x_train: 训练数据
    y_train: 训练数据的目标值
    x_test: 测试数据
    '''
    clf = SVC(C=C, kernel=kernelfunc)
    clf.fit(x_train, y_train)
    y_pred = clf.predict(x_test)
    return y_pred

def SVMRegression(x_train, y_train, x_test, C, kernelfunc):
    '''
    x_train: 训练数据
    y_train: 训练数据的目标值
    x_test: 测试数据
    '''
    reg = SVR(C=C, kernel=kernelfunc)
    reg.fit(x_train, y_train)
    y_pred = reg.predict(x_test)
    return y_pred
