#!/usr/bin/env python
#-*- coding:utf-8 -*-

'read file'

__author__='Peng BinBin'

import sys
# from PIL import Image
import numpy

from sklearn.cluster import KMeans

def pccCaculate(item1,item2):
    sum1=0
    sum2=0
    sum3=0
    # for item in item1.values():
    #     sum1=sum1+int(item)
    # for item in item2.value():
    #     sum2=sum2+int(item)
    # for item in range(len(item1)):
    for item in item1:
        sum1 = sum1 + int(item1[item])
        sum2 = sum2 + int(item2[item])
        # print item1[item]
    avg1=sum1/len(item1)
    avg2=sum2/len(item2)
    sum1=0
    sum2=0
    for item in item1:
        sum1=sum1+numpy.square(int(item1[item])-avg1)
        sum2=sum2+numpy.square(int(item2[item])-avg2)
        sum3=sum3+(int(item1[item])-avg1)*(int(item2[item])-avg2)
    similar=0
    if sum1!=0 and sum2!=0 and sum3!=0:
        similar=sum3/numpy.sqrt(sum1*sum2)
    # print similar
    return similar

def kmeans(k,user_rating):
    tempitem=[]
    tempitem1={}
    tempitem2={}
    cluster=[]#所有的K个cluster
    clusterChild=[]#每个cluster中包含的用户
    clusterCentroid=[]#cluster的中点
    changeFlag=1

    for i in range(k):
        # cluster[i]=[]
        # clusterCentroid[k]=[]
        # print i, k, user_rating[i]
        clusterChild.append(user_rating[i])
        cluster.append(clusterChild)
        clusterCentroid.append(user_rating[i])

    while(changeFlag==1):
        changeFlag=0

        for item in user_rating:
            i=0
            for item2 in clusterCentroid:
                for itemKey in item:
                    if itemKey in item2.keys():
                        tempitem1[itemKey]=item[itemKey]
                        tempitem2[itemKey]=item2[itemKey]
                if len(tempitem1)!=0:
                    tempitem.append(pccCaculate(tempitem1,tempitem2))
                else :
                    tempitem[i]=0
                if i==tempitem.index(max(tempitem)):
                    changeFlag=1
                cluster[i].append(item)
                i=i+1
        clusterCentroid=[]
        sumTemp=[]
        sumTempChild = {}
        for i in range(k):
            sumTemp.append(sumTempChild)
        for i in range(k):
            sumTemp[i]={}
            for item in cluster[i]:
                for itemDictKey in item:
                    sumTemp[i][itemDictKey]=0#将评分矩阵中的分数转换为整型
                    if itemDictKey in sumTemp[i].keys():
                        sumTemp[i][itemDictKey]+=int(item[itemDictKey])
                    else:
                        sumTemp[i][itemDictKey]=int(item[itemDictKey])
            for item in sumTemp[i]:
                sumTemp[i][item]=sumTemp[i][item]/len(cluster[i])
            clusterCentroid.append(sumTemp[i])
        print clusterCentroid,

    print '\n'
    print clusterCentroid

def readFile():
    file='0'
    user_rating=[]
    movieItem=[]
    user={}
    with open('ratings.dat') as f:
            ratingItem=f.readlines()
    i=0
    for item in ratingItem:
        usertemp=item.split('::')
        # user[user]=usertemp
        if(int (usertemp[0])==i):
            user[usertemp[1]]=usertemp[2]
        else:
            user['user']=str(int(usertemp[0])-1)
            if len(user)!=1:
                user_rating.append(user)
            user={}
            i=i+1
            continue
    # print user_rating
    return user_rating

if __name__=='__main__':
    user_rating=readFile()
    print len(user_rating[0])

    kmeans(10,user_rating)