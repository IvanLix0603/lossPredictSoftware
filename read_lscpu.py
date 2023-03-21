import pandas as pd
import numpy as np
import os
import json


def preprocess() -> pd.DataFrame:
    df = read_cpu()
    data = dict()
    a = float(df['CPU(s)'].split('-')[1])
    data['CPU(s)'] = a
    
    lis = ['CPU MHz', 'CPU MHz', 'CPU max MHz', 'CPU min MHz']
    for i in lis:
        data[i] = cpu_MHz(df[i])
    
    lis = ['L1d cache', 'L1i cache', 'L2 cache', 'L3 cache']
    for i in lis:
          data[i] = caches(df[i])

    data_to_nn = pd.DataFrame(data, index=[0])#, , 'CPU MHz', 'CPU max MHz', 'CPU min MHz','L1d cache', 'L1i cache', 'L2 cache', 'L3 cache'])
   
    return data_to_nn


def read_cpu():
    words = ['Architecture', 'CPU(s)', 'CPU MHz', 'CPU max MHz', 'CPU min MHz', 'L1d cache', 'L1i cache', 'L2 cache', 'L3 cache']
    #words =['Архитектура', 'CPU(s):', 'CPU MHz', 'CPU max MHz', 'CPU min MHz:', 'L1d cache', 'L1i cache', 'L2 cache', 'L3 cache']
     
    os.system('lscpu > lscpuf')
    f = 'lscpuf'
    res = dict()
    for i in range(len(words)):
        res[f'{words[i]}'] = '0,0'
    with open(f, 'r') as f:
           for line in f:
            for i in range(len(words)):
                if words[i] in line:
                    l = line.split(':')[1].replace(' ', '').replace('\n', '')
                    res[f'{words[i]}'] = l   
    
    os.system('rm lscpuf')
    return res


def cpu_MHz(a):
    b = float(a.split(',')[0])
    return b

def caches(a):
    if 'K' in a:
        b = float(a.split('K')[0])*1024
    if 'M' in a:
        b = float(a.split('M')[0])*1024*1024 
    return b

def hnool(a, around=False):
    if around == True:
        b = np.append(np.around(float(a), 2), b)
        return b
    b = float(b)
    return b
