from numpy import *

fileData=open("/root/operrecord_18062410.txt")

dataTemp=[]

for line in fileData.readlines():

    lineData=line.strip('\n').split(',')
    lineDataDealed=map(float,lineData)
    print(lineDataDealed)



