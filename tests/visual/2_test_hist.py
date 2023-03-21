import numpy as np 
import matplotlib.pyplot as plt
import os
import sys

def decimation(a):
    for i in range(len(a)):
        if a[i] <= 0:
            a[i] = 0
    return a


def preprocess_data(dir):
    files = []
    os.chdir(dir)########3
    time_0 = []
    time_1 = []
    for _, _, files in os.walk(".", topdown = False):
        for file in files:
            if 'time' and '_O0' in file:
                time_0.append(file)
            if 'time' and '_O1' in file:
                time_1.append(file)
    return sort_data(time_0), sort_data(time_1)

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
    result_data = dict()
    time_0, time_1 = preprocess_data('2_test')    
    for files in zip(time_0, time_1):
        data = exctract_data(files)
        calc_time = calculation_time(data[0], data[1], data[2])
        result_data[data[2]] = calc_time  ###################      
    os.chdir('../')
    draw_plot(result_data, N)
    #plt.hist(result_data[0][0])
    os.chdir('../')

    pass 

def exctract_data(files): 
    time = np.loadtxt(os.path.abspath(files[0]))
    time_prev = np.loadtxt(os.path.abspath(files[1]))
    maxi = parser_name_files(files[0]) 
    data = (time, time_prev, maxi)
    return data

def parser_name_files(file):
    number = file.split('_')[1] 
    return int(number)

def calculation_time(time_0, time_1, maxi):    
    '''
    del_null = lambda x: x+0.0001
    time_0 = del_null(time_0)
    time_1 = del_null(time_1)
    prof_t0 = 1/time_0
    prof_t1 = 1/time_1
    delta_prof = abs(prof_t1 - prof_t0)+0.00001 #############
    relation_prof = (delta_prof/prof_t1) * 100##########
    '''
    time_0 = np.array(time_0)
    time_1 = np.array(time_1)
    delta_prof = np.subtract(time_0, time_1) #############
    delta_prof = decimation(delta_prof)
    relation_prof = (delta_prof/time_1) * 100#########
    print(relation_prof)
    relation_prof = np.array([sum(relation_prof)/len(relation_prof)])
    os.chdir('../')
    np.savetxt(f'delta_2_test_{maxi}.txt', relation_prof)
    os.system(f'cp delta_2_test_{maxi}.txt ../db')
    os.chdir('2_test/')
    #print(relation_time)
    return relation_prof

def draw_plot(data, NEl):
    x_name = [*NEl]
    n_rows = len(NEl)
    N = np.arange(len(x_name))
    for i in range(len(x_name)):
        plt.bar(N[i], data[x_name[i]])
    plt.xticks(N, x_name)
    plt.title('Отображение резултатов 2 теста')
    plt.xlabel('Количество элементов')
    plt.ylabel('Потери во времени, %')
    plt.grid()
    #plt.show()
    plt.savefig("Отображение результатов 2 теста")

def get_from_manager(N):
    ind_n= ['25', '50', '100', '150', '200']
    result_N = []
    for i in ind_n:
        if i in N:
            result_N.append(int(i))
    return  result_N

if __name__=='__main__':
    N = sys.argv[1]
    N = get_from_manager(N)
    main(N)