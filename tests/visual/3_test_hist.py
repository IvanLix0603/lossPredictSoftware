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
    os.chdir(dir)
    time = []
    for _, _, files in os.walk(".", topdown = False):
        for file in files:
            if 'time' in file:
                time.append(file)
    os.chdir('../')
    return sort_data(time)#, sort_data(var)

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
    time_prev = preprocess_data('1_test')###my data
    result_data = list()
    time = preprocess_data('3_test')    
    for files in zip(time, time_prev):
        data = exctract_data(files)
        calc_time = calculation_time(data[0], data[1], data[2])
        result_data.append([calc_time, data[2]])         
    draw_plot(result_data, N)
    #plt.hist(result_data[0][0])
    os.chdir('../')####

    pass 

def exctract_data(files):
    os.chdir('3_test')
    time = np.loadtxt(os.path.abspath(files[0]))
    os.chdir('../1_test')
    time_prev = np.loadtxt(os.path.abspath(files[1]))
    os.chdir('../')
    maxi = parser_name_files(files[0]) 
    data = (time, time_prev, maxi)
    return data

def parser_name_files(file): 
    number = file.split('_')[1] 
    return int(number)

def calculation_time(sp_time, wsp_time, maxi):    
    '''   
    prof_sp = 1/sp_time
    prof_wsp = 1/wsp_time
    delta_prof = abs(prof_sp - prof_wsp) #############
    relation_prof = (delta_prof/prof_wsp) * 100##########
    '''
    sp_time += 0.0001
    wsp_time += 0.0001
    sp_time = np.array(sp_time)
    wsp_time = np.array(wsp_time)
    delta_prof = np.subtract(sp_time, wsp_time) #############
    delta_prof = decimation(delta_prof)
    relation_prof = (delta_prof/wsp_time) * 100#########
    print(relation_prof)
    relation_prof = np.array([sum(relation_prof)/len(relation_prof)])
    np.savetxt(f'delta_3_test_{maxi}.txt', relation_prof)
    os.system(f'cp delta_3_test_{maxi}.txt ../db')
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
    plt.savefig('Отображение результатов 3 теста', dpi=100)

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

