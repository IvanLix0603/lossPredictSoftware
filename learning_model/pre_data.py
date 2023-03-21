import pandas as pd
import numpy as np


def launch() -> pd.DataFrame:
    data = dict()
    df = pd.read_csv('big_data.csv')
    a = df['CPU(s)'].to_list()
    cpus = np.array([])
    for i in a: 
        i = str(i)

        if ',' in i:
            i = i.split(',')[1]

        if '-' in i: 
            i = float(i.split('-')[1]) 
        b = float(i)
        
        cpus = np.append(b, cpus)
    data['CPU(s)'] = cpus
    
    lis = ['CPU MHz', 'CPU MHz', 'CPU max MHz', 'CPU min MHz']
    for i in lis:
        data[i] = cpu_MHz(df[i].to_list())
    
    lis = ['L1d cache', 'L1i cache', 'L2 cache', 'L3 cache']
    for i in lis:
          data[i] = caches(df[i].to_list())

    lis = ['hyper_thread', 'N', 'O1', 'O2', 'test_number']
    for i in lis:
        data[i] = hnool(df[i].to_list())
    data['loss'] = hnool(df['loss'].to_list(), around=True)
    
    '''
    x = list(data.values())[:-1]
    y = list(data.values())[-1]
    z = [i for i in zip(x, y)]
    data_to_nn = np.array(z)
    '''
    data_to_nn = pd.DataFrame(data)
    #print(data_to_nn)


    return data_to_nn


def cpu_MHz(a) -> np.array:
    b = np.array([])
    for i in a:
        c = float(i.split(',')[0])
        b = np.append(c, b)
    return b

def caches(a) -> np.array:
    b = np.array([])
    for i in a:
        c = i.split('i')[0]
        if 'K' in i:
            c = float(i.split('K')[0])*1024
            b = np.append(c, b)
        if 'M' in i:
            c = float(i.split('M')[0])*1024*1024
            b = np.append(c, b)
    return b

def hnool(a, around=False) -> np.array:
    if around == True:
        b = np.array([])
        for i in a:
            b = np.append(np.around(float(i), 2), b)
        return b
    b = np.array([])
    for i in a:
        b = np.append(float(i), b)
    return b


if __name__ == '__main__':
    launch()
 
