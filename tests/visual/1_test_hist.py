from statistics import mean
import numpy as np 
import matplotlib.pyplot as plt
import os
from poly import PolyPredict 
import sys

def decimation(a):
    for i in range(len(a)):
        if a[i] <= 0:
            a[i] = 0
    return a


def preprocess_data():
    files = []
    os.chdir("1_test")########3
    time = []
    var = []
    for _, _, files in os.walk(".", topdown = False):
        for file in files:
            if 'time' in file:
                time.append(file)
            if 'var' in file:
                var.append(file)
    return sort_data(time), sort_data(var)

def sort_data(tmp):
    tmp = np.array(tmp)
    index = np.array([])
    for i in tmp:
        m = int(i.split('_')[1])
        index = np.append(index, m)
    sor = np.argsort(index)
    tmp = tmp[sor]
    return list(tmp)

def main(N):
    result_data = list()
    time, var = preprocess_data()    
    for files in zip(time, var):
        #print(files)
        data = exctract_data(files)
        lin_data = linear(data)
        calc_time = calculation_time(data[0], lin_data, data[2])
        result_data.append([calc_time, data[2]])         
    os.chdir('../')#####
    draw_plot(result_data, N)
    os.chdir('../')
    pass 

def exctract_data(files):
    time = np.loadtxt(os.path.abspath(files[0]))
    means = np.loadtxt(os.path.abspath(files[1]))
    maxi = parser_name_files(files[0]) 
    data = (time, means, maxi)
    return data

def parser_name_files(file): 
    number = file.split('_')[1] 
    return int(number)


def linear(data):
    x = data[1]
    y = data[0]
    model = PolyPredict(x, y)
    pred = model.predict()
    return abs(pred)

def calculation_time(fact_time, expect_time, maxi):    
    #prof_fact = 1/fact_time
    #prof_expect = 1/expect_time
    #delta_prof = abs(prof_fact - prof_expect) #############
    #relation_prof = (delta_prof/prof_expect) * 100##########
    fact_time = np.array(fact_time)
    expect_time = np.array(expect_time)
    delta_prof = np.subtract(fact_time, expect_time) #############
    delta_prof = decimation(delta_prof)
    relation_prof = (delta_prof/expect_time) * 100#########
    print(relation_prof)
    relation_prof = np.array([sum(relation_prof)/len(relation_prof)])
    os.chdir('../')
    np.savetxt(f'delta_1_test_{maxi}.txt', relation_prof)
    os.system(f'cp delta_1_test_{maxi}.txt ../db')
    os.chdir('1_test/')
    return relation_prof

def draw_plot(data, NEl):
    x_name = [*NEl]
    n_rows = len(NEl)
    N = np.arange(len(x_name))
    for row in range(n_rows):
        plt.bar(N[row], data[row][0])
    plt.title('Отображение результатов 1 теста')
    plt.xticks(N, x_name)
    plt.xlabel('Количество элементов')
    plt.ylabel('Потери во времени, %')
    plt.grid()
    #plt.show()
    plt.savefig('Отображение результатов 1 теста', dpi=100)

def get_from_manager(N):
    ind_n= ['25', '50', '100', '150', '200', '300', '500', '1000', '1200']
    result_N = []
    for i in ind_n:
        if i in N:
            result_N.append(int(i))
    return  result_N

if __name__=='__main__':
    N = sys.argv[1]
    N = get_from_manager(N)
    main(N)
