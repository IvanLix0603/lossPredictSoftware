#!/usr/bin/python3
###SEPARATE ON H, M, S#####
import numpy as np
import matplotlib.pyplot as plt
import sys
from poly import PolyPredict


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
    draw_plot(time, num_vars)
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

def draw_plot(time, num_vars):
    #Полимномиальная регрессия
    
    model = PolyPredict(num_vars, time)
    time_pred = model.predict()
    print('Полимномиальная регрессия')
     
    fig = plt.figure()
    fig.canvas.set_window_title('График')
    ax = fig.add_subplot(1, 1, 1)
    print(num_vars.shape == time_pred.shape)
    ax.plot(num_vars, time, color='tab:blue', linewidth=2, linestyle='--')
    ax.plot(num_vars, time_pred, color='tab:orange', linewidth=2)
    
    ax.set_xlim([0,max(num_vars)+1])
    ax.set_ylim([0,max(time)+0.1])
    ax.set_title('Зависимость времени выполнения linpack_64 от размеров матрицы')
    ax.set_xlabel("Размер матрицы, N")
    ax.set_ylabel("Время, с")
    ax.grid(True)
    
    
    
    if max(num_vars)<=100: step_x=5
    elif max(num_vars)<=200: step_x=10
    elif max(num_vars)<=500: step_x=25
    elif max(num_vars)<=750: step_x=50
    else: step_x=100
    
    if max(time)<=1: step_y=0.05
    elif max(time)<=2.5: step_y=0.1
    elif max(time)<=5: step_y=0.2
    else: step_y=0.5
    
    
    xticks = np.arange(0,max(num_vars)+1,step_x)
    yticks = np.arange(0,max(time)+0.1, step_y)
    ax.set_xticks(xticks)
    ax.set_yticks(yticks)
    ax.legend()
    #plt.show()
    name_pic='pictures/'+str(max(num_vars))+'.png'
    name_pic=str(max(num_vars))+'.png'
    fig.savefig(name_pic)
    
    name_vars='results/vars_'+str(max(num_vars))
    name_time='results/time_'+str(max(num_vars))
    np.savetxt(name_vars,num_vars)
    np.savetxt(name_time,time)
    
    #Сделаем линейную регрессию
    #if max(num_vars)>=100:


if __name__== '__main__':
    files_list = []
    for i in range(1, 3):
        files_list.append(sys.argv[i])
    prepare(files_list)
