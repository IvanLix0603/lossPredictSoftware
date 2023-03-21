import sqlite3 as sql3
import sys
import json
import os
import numpy as np


def parse_cpu(file):
    f = open(file, 'r')
    data = json.load(f)
    f.close()
    print(data)
    #task = [f'{data["Architecture"]}, {data["CPU(s):"]}, {data["CPU MHz"]}, {data["CPU max MHz"]}, {data["CPU min MHz:"]}, {data["L1d cache"]}, {data["L1i cache"]}, {data["L2 cache"]}, {data["L3 cache"]}, {bool(1)}'
    task = [data["Architecture"], data["CPU(s)"], data["CPU MHz"], data["CPU max MHz"], data["CPU min MHz"], data["L1d cache"], data["L1i cache"], data["L2 cache"], data["L3 cache"], bool(1)]
    return task

def parse_delta(file) -> tuple :
    task_n = file.split('_')[-1].split(".")[0]
    print(task_n)
    data = np.loadtxt(os.path.abspath(file))
    task_delta = data#del
    print(task_delta)#del
    return task_delta, task_n


def mainly(test, N):
    conn = sql3.connect('data.db')
    cursor = conn.cursor()
    files = ['cpuinfo.json']
    for i in range(len(N)):
            files.append(f'delta_{test}_test_{N[i]}.txt')
            
    task_cpu = parse_cpu(files[0]) 
    for i in files[1:len(N)]:
        task_delta, task_n = parse_delta(i)
        task_delta = str(task_delta)
        task_n = str(task_n)
        task_test = str(test)
        if test == 2:
            task_O1 = str(0)
            task_O2 = str(1)
        else:
            task_O1 = str(1)
            task_O2 = str(0)
        sql = 'INSERT INTO results(arch, cpus, CPU_MHz, CPU_max_MHz, CPU_min_MHz, L1d_cashe, L1i_cashe, L2_cashe, L3_cashe, hyper_thread, N, O1, O2, test_number, loss) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
        #task =  (task_cpu + ', ' + task_n + ', ' + task_O1 + ', ' + task_O2 + ', ' +task_test + ', ' + task_delta)
        task = [*task_cpu, task_n, task_O1, task_O2, task_test, task_delta]
        print(task)
        #conn = sql3.connect('data.db')
        #cursor = conn.cursor()
        cursor.execute(sql, task)
    conn.commit()
    conn.close()
    
def get_from_manager(N):
    ind_n= ['25', '50', '100', '150', '200', '300', '500', '1000', '1200']
    result_N = []
    for i in ind_n:
        if i in N:
            result_N.append(int(i))
    return  result_N
        
            

if  __name__== '__main__':
    N = sys.argv[2]
    N = get_from_manager(N)
    mainly(sys.argv[1], N)
