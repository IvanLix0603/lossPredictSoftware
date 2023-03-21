#!/usr/bin/python3
###SEPARATE ON H, M, S#####
#import numpy as np
import sys

def prepare(files_list):
    data = [[],[]]
    #print(files_list)
    for i in range(2):    
        with open(files_list[i], "r") as file:
            for line in file:
                data[i].append(file.read())

    time = parser_time(data[0])
    num_vars = parser_data(data[1]) ####ready
    #print(time, num_vars)
    save_data(time, num_vars)
    pass

def parser_time(time):
    time = time[0].split('\n')
    time.pop(-1)
    tmp = []
    for i in time:
        tmp_i = 0
        m = i.split('m')
        t = float(m[0])
        tmp_i += t*60
        m[1]=m[1].replace(',','.')
        sec = float(m[1].split('s')[0])
        #print(sec)
        tmp_i += sec
        tmp.append(tmp_i)
    time = tmp
    return time

def parser_data(data):
    tmp = data[0].split('\n')
    tmp.pop(-1)
    #print(tmp)
    num_vars = []
    for i in range(len(tmp)):
        num_vars.append(int(tmp[i]))
    #num_vars = np.array(num_vars)
    return num_vars

    
    
def save_data(time, num_vars):
    name_vars_f='results/vars_'+str(max(num_vars))
    name_time='results/time_'+str(max(num_vars))
    with open(name_vars_f, 'w') as nvf:
        for i in num_vars:
            nvf.writelines(str(i))
            nvf.writelines('\n')
    with open(name_time, 'w') as nvt:
        for i in time:
            nvt.writelines(str(i))
            nvt.writelines('\n')
    


if __name__== '__main__':
    files_list = []
    for i in range(1, 3):
        files_list.append(sys.argv[i])
    prepare(files_list)
