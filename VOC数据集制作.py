# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 16:04:33 2018

@author: asus
"""

import os
import random 
#先划分训练集+验证集(0.8)和测试集,再将训练集+验证集划分开(一样一半)
trainval_percent = 0.8 
train_percent = 0.7 
xmlfilepath = 'C:\\Users\\asus\\Desktop\\Annotations' 
txtsavepath = 'C:\\Users\\asus\\Desktop\\ImageSets\\Main' 
total_xml = os.listdir(xmlfilepath) 

num=len(total_xml) 
tv=int(num*trainval_percent)#训练集+验证集
tr=int(tv*train_percent) #训练集
trainval= random.sample(range(num),tv) 
train=random.sample(trainval,tr) 

ftrainval = open('C:\\Users\\asus\\Desktop\\ImageSets\\Main\\trainval.txt', 'w') 
ftest = open('C:\\Users\\asus\\Desktop\\ImageSets\\Main\\test.txt', 'w') 
ftrain = open('C:\\Users\\asus\\Desktop\\ImageSets\\Main\\train.txt', 'w') 
fval = open('C:\\Users\\asus\\Desktop\\ImageSets\\Main\\val.txt', 'w') 

for i in range(num):
    name=total_xml[i][:-4]+'\n' 
    if i in trainval: 
        ftrainval.write(name) 
        if i in train: 
            ftrain.write(name) 
        else:
            fval.write(name)
    else:
        ftest.write(name) 

ftrainval.close()
ftrain.close()
fval.close()
ftest.close()