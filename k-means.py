import numpy as np
import math

import matplotlib.pyplot as plt
import matplotlib.cm as cm

import csv

"""
#计算两个经纬度之间的距离
def distCalculation(vecA,vecB):
    Lat1=math.radians(vecA[0][0,1])
    Lat2=math.radians(vecB[0][0,1])
    a=Lat1-Lat2
    b=math.radians(vecA[0][0,0])-math.radians(vecB[0][0,0])
    s = 2 * math.asin(math.sqrt(math.pow(math.sin(a / 2), 2) + math.cos(Lat1)*math.cos(Lat2)*math.pow(math.sin(b / 2), 2)))
    distance=s*6378137
    return distance



# 构建聚簇中心，取k个随机质心
def randCent(dataSet, k):
    n = np.shape(dataSet)[1]
    centroids = np.mat(np.zeros((k,n)))   # 每个质心有n个坐标值，总共要k个质心
    for j in range(n):
        minJ = min(dataSet[:,j])
        maxJ = max(dataSet[:,j])
        rangeJ = float(maxJ - minJ)
        centroids[:,j] = minJ + rangeJ * np.random.rand(k, 1)
    return centroids


# 加载数据
def loadDataSet(fileName):  # 解析文件，得到一个浮点数字类型的矩阵
    totalDataMat = []              # 文件的最后一个字段是类别标签
    fr = open(fileName)
    for line in fr.readlines():
        curLine = line.strip('\n').split(',')
        fltLine = list(map(float, curLine))    # 将每个元素转成float类型
        totalDataMat.append(fltLine)
    return np.mat(totalDataMat)


# k-means 聚类算法
def kMeans(dataSet, k, distMeans =distCalculation, createCent = randCent):
    m = np.shape(dataSet)[0]
    clusterAssment = np.mat(np.zeros((m,2)))    # 用于存放该样本属于哪类及质心距离
    # clusterAssment第一列存放该数据所属的中心点，第二列是该数据到中心点的距离
    centroids = createCent(dataSet, k)
    clusterChanged = True   # 用来判断聚类是否已经收敛
    Terminator=[]
    for i in range(k):
        Terminator.append([])
    while clusterChanged:
        clusterChanged = False
        for i in range(m):  # 把每一个数据点划分到离它最近的中心点
            minDist = np.inf; minIndex = -1
            for j in range(k):
                distJI = distMeans(centroids[j,:], dataSet[i,:])
                if distJI < minDist:
                    minDist = distJI; minIndex = j  # 如果第i个数据点到第j个中心点更近，则将i归属为j
            Terminator[minIndex].append(i)

    return centroids,Terminator




# --------------------测试----------------------------------------------------
# 用测试数据及测试kmeans算法
datMat = loadDataSet('C:\\Users\\Rooobins\\Desktop\\operrecord_18062410.txt')
myCentroids,clustAssing = kMeans(datMat,500)



colors=iter(cm.rainbow(np.linspace(0,1,len(clustAssing))))
x=[]
y=[]
for listData in clustAssing:
    x.clear()
    y.clear()
    for i in listData:
        x.append(datMat[i,0])
        y.append(datMat[i,1])

    plt.scatter(x,y,color=next(colors))


plt.show()


writeClustAssing=open("C:\\Users\\Rooobins\\Desktop\\clustAssing.txt",'w+')
writeClustAssing.writelines(str(clustAssing))
writeClustAssing.close()

"""





with open("C:\\Users\\Rooobins\\Desktop\\data.csv",'w+')  as csvfile:
    import csv

    with open("C:\\Users\\Rooobins\\Desktop\\data.csv",'w+') as csvfile:
        spamwriter = csv.writer(csvfile, dialect='excel')
        # 读要转换的txt文件
        with open("C:\\Users\\Rooobins\\Desktop\\operrecord_18062410.txt", 'r+') as filein:
            for line in filein:
                line_list = line.strip().split()
                spamwriter.writerow(line_list)





