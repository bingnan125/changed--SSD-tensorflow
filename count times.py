# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 11:03:58 2018

@author: Bona
"""
import xml.dom.minidom
import os
TRAIN_STATISTICS = {
    'none': [0, 0],
    '0': [0, 0],  #238图片书， 306目标总数
    '1': [0, 0],
    '2': [0, 0],
    '3': [0, 0],
    '4': [0, 0],
    '5': [0, 0],
    '6': [0, 0],
    '7': [0, 0],
    '8': [0, 0],
    '9': [0, 0],
    'total': [0, 0]
}

TEST_STATISTICS = {
    'none': [0, 0],
    '0': [0, 0],  #238图片书， 306目标总数
    '1': [0, 0],
    '2': [0, 0],
    '3': [0, 0],
    '4': [0, 0],
    '5': [0, 0],
    '6': [0, 0],
    '7': [0, 0],
    '8': [0, 0],
    '9': [0, 0],
    'total': [0, 0]
}


#打开xml文档
path = 'C:\\Users\\asus\\Desktop\\SSD-Tensorflow\\imagedata\\VOCdevkit\\VOC\\Annotations'
files = os.listdir(path)
for file in files:
    dom = xml.dom.minidom.parse(os.path.join(path,file))
    #得到文档元素对象
    root = dom.documentElement

    #获得子标签的标签name
    folder = root.getElementsByTagName('folder')
    filename = root.getElementsByTagName('filename')
    name = root.getElementsByTagName('name')
    b1= folder[0]
    f1= filename[0].firstChild.data.split('.')[0]
    f1_set = ''.join(x for i, x in enumerate(f1) if f1.index(x) == i)
    
    #获得标签对之间的数据
    print(b1.firstChild.data)
    if b1.firstChild.data=='test':
        TEST_STATISTICS['total'][0]+=1
    else:
        TRAIN_STATISTICS['total'][0]+=1
    if b1.firstChild.data=='test':
        for item in f1_set:
            TEST_STATISTICS[item][0]+=1
        for i in range(len(name)):
            c1= name[i]
            TEST_STATISTICS[c1.firstChild.data][1]+=1
            TEST_STATISTICS['total'][1]+=1
    else:
        for item in f1_set:
            TRAIN_STATISTICS[item][0]+=1
        for i in range(len(name)):
            c1= name[i]
            TRAIN_STATISTICS[c1.firstChild.data][1]+=1
            TRAIN_STATISTICS['total'][1]+=1


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""分隔线""""""""""""""""""""""""""""""""分隔线""""""""""""""""""""""""""""""分隔线""""""""""
"""""""""分隔线""""""""""""""""""""""""""""""""分隔线""""""""""""""""""""""""""""""分隔线""""""""""
"""""""""分隔线""""""""""""""""""""""""""""""""分隔线""""""""""""""""""""""""""""""分隔线""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""



import os
path = 'C:\\Users\\asus\\Desktop\\SSD-Tensorflow\\imagedata\\VOCdevkit\\VOC\\ImageSets\\Main'
train = open(os.path.join(path,'train.txt'))
TRAIN_STATISTICS = {
    'none': [0, 0],
    '0': [0, 0],  #238图片书， 306目标总数
    '1': [0, 0],
    '2': [0, 0],
    '3': [0, 0],
    '4': [0, 0],
    '5': [0, 0],
    '6': [0, 0],
    '7': [0, 0],
    '8': [0, 0],
    '9': [0, 0],
    'total': [0, 0]
}
lines = train.readlines()
for line in lines:
    line = line.strip()
    print(line)
    line_set = ''.join(x for i, x in enumerate(line) if line.index(x) == i)
    for ele in line:
        TRAIN_STATISTICS[ele][1]+=1
        TRAIN_STATISTICS['total'][1]+=1
    for item in line_set:
        TRAIN_STATISTICS[item][0]+=1
TRAIN_STATISTICS['total'][0]=len(lines)
train.close()



test = open(os.path.join(path,'test.txt'))
TEST_STATISTICS = {
    'none': [0, 0],
    '0': [0, 0],  #238图片书， 306目标总数
    '1': [0, 0],
    '2': [0, 0],
    '3': [0, 0],
    '4': [0, 0],
    '5': [0, 0],
    '6': [0, 0],
    '7': [0, 0],
    '8': [0, 0],
    '9': [0, 0],
    'total': [0, 0]
}
lines = test.readlines()
for line in lines:
    line = line.strip()
    print(line)
    line_set = ''.join(x for i, x in enumerate(line) if line.index(x) == i)
    for ele in line:
        TEST_STATISTICS[ele][1]+=1
        TEST_STATISTICS['total'][1]+=1
    for item in line_set:
        TEST_STATISTICS[item][0]+=1
TEST_STATISTICS['total'][0]=len(lines)
test.close()

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""分隔线""""""""""""""""""""""""""""""""分隔线""""""""""""""""""""""""""""""分隔线""""""""""
"""""""""分隔线""""""""""""""""""""""""""""""""分隔线""""""""""""""""""""""""""""""分隔线""""""""""
"""""""""分隔线""""""""""""""""""""""""""""""""分隔线""""""""""""""""""""""""""""""分隔线""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

    
import os
path = 'C:\\Users\\asus\\Desktop\\SSD-Tensorflow\\imagedata\\VOCdevkit\\VOC\\JPEGImages'

files = os.listdir(path)
TRAIN_STATISTICS = {
    'none': [0, 0],
    '0': [0, 0],  #238图片书， 306目标总数
    '1': [0, 0],
    '2': [0, 0],
    '3': [0, 0],
    '4': [0, 0],
    '5': [0, 0],
    '6': [0, 0],
    '7': [0, 0],
    '8': [0, 0],
    '9': [0, 0],
    'total': [0, 0]
}
for file in files:
    num_set = ''.join(x for i, x in enumerate(file.split('.')[0]) if file.split('.')[0].index(x) == i)
    for ele in file.split('.')[0]:
        TRAIN_STATISTICS[ele][1]+=1
        TRAIN_STATISTICS['total'][1]+=1
    for item in num_set:
        TRAIN_STATISTICS[item][0]+=1
TRAIN_STATISTICS['total'][0]=len(files)     
