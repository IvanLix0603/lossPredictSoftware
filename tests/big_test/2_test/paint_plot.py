#!/usr/bin/python3
###SEPARATE ON H, M, S#####
import numpy as np
import matplotlib.pyplot as plt
import sys

def prepare(files_list):
    print (files_list)
    #для варианта О0
    data_0 = [[],[]]
    for i in range(2):    
        with open(files_list[i], "r") as file:
            for line in file:
                data_0[i].append(file.read())

    time_0 = parser_time(data_0[0])
    num_vars_0 = parser_data(data_0[1]) 
    
    #для варианта О1
    data_1 = [[],[]]
    for i in range(2,4):    
        with open(files_list[i], "r") as file:
            for line in file:
                data_1[i-2].append(file.read())

    time_1 = parser_time(data_1[0])
    num_vars_1 = parser_data(data_1[1]) 

    #для варианта О2
    data_2 = [[],[]]
    for i in range(4,6):    
        with open(files_list[i], "r") as file:
            for line in file:
                data_2[i-4].append(file.read())

    time_2 = parser_time(data_2[0])
    num_vars_2 = parser_data(data_2[1]) 
    draw_plot(time_0, num_vars_0,time_1, num_vars_1,time_2, num_vars_2)
    
    
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
    time = np.array(tmp)
    return time

def parser_data(data):
    tmp = data[0].split('\n')
    tmp.pop(-1)
    #print(tmp)
    num_vars = []
    for i in range(len(tmp)):
        num_vars.append(int(tmp[i]))
    num_vars = np.array(num_vars)
    return num_vars

def draw_plot(time_0, num_vars_0,time_1, num_vars_1,time_2, num_vars_2):
     
    fig = plt.figure()
    fig.canvas.set_window_title('График')
    ax = fig.add_subplot(1, 1, 1)
    
    ax.plot(num_vars_0, time_0, color='tab:red', linewidth=2,label='уровень опитимизации О0')
    ax.plot(num_vars_1, time_1, color='tab:green', linewidth=2,label='уровень опитимизации О1')
    ax.plot(num_vars_2, time_2, color='tab:orange', linewidth=2,label='уровень опитимизации О2')
    ax.legend(loc='upper left')
        

    ax.set_xlim([0,max(num_vars_0)+1])
    ax.set_ylim([0,max(time_0)+0.1])
    ax.set_title('Зависимость времени выполнения linpack_64 от размеров матрицы')
    ax.set_xlabel("Размер матрицы, N")
    ax.set_ylabel("Время, с")
    ax.grid(True)
    
    
    
    if max(num_vars_0)<=100: step_x=5
    elif max(num_vars_0)<=200: step_x=10
    elif max(num_vars_0)<=500: step_x=25
    elif max(num_vars_0)<=750: step_x=50
    else: step_x=100
    
    if max(time_0)<=1: step_y=0.05
    elif max(time_0)<=2.5: step_y=0.1
    elif max(time_0)<=5: step_y=0.2
    else: step_y=0.5
    
    
    xticks = np.arange(0,max(num_vars_0)+1,step_x)
    yticks = np.arange(0,max(time_0)+0.1, step_y)
    ax.set_xticks(xticks)
    ax.set_yticks(yticks)
    ax.legend()
    #plt.show()
    name_pic='pictures/'+str(max(num_vars_0))+'.png'
    fig.savefig(name_pic)

    name_vars='results/vars_'+str(max(num_vars_0))+'_O0'
    name_time='results/time_'+str(max(num_vars_0))+'_O0'
    np.savetxt(name_vars,num_vars_0)
    np.savetxt(name_time,time_0)
    name_vars='results/vars_'+str(max(num_vars_1))+'_O1'
    name_time='results/time_'+str(max(num_vars_1))+'_O1'
    np.savetxt(name_vars,num_vars_1)
    np.savetxt(name_time,time_1)
    name_vars='results/vars_'+str(max(num_vars_2))+'_O2'
    name_time='results/time_'+str(max(num_vars_2))+'_O2'
    np.savetxt(name_vars,num_vars_2)
    np.savetxt(name_time,time_2)



if __name__== '__main__':
    files_list = []
    for i in range(1, 7):
        files_list.append(sys.argv[i])
    prepare(files_list)
