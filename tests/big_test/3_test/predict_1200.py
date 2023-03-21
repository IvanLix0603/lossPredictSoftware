import numpy as np
import pandas as pd
from poly import PolyPredict
import matplotlib.pyplot as plt
import sys

def main_1200(N):
    #time = pars_time()
    time = np.loadtxt(f'results/time_{N[-1]}')
    num_vars = np.loadtxt(f'results/vars_{N[-1]}')
    model = PolyPredict(num_vars, time)
    time_pred, num_vars_pred = model.predict(f1200=True)
    #draw_plot
    fig = plt.figure()
    fig.canvas.set_window_title('График')
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(num_vars, time, color='tab:blue', linewidth=2, linestyle='--')
    ax.plot(num_vars_pred, time_pred, color='tab:orange', linewidth=2)
    


    ax.set_xlim([0,max(num_vars_pred)+1])
    ax.set_ylim([0,max(time_pred)+0.1])
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
    
    
    xticks = np.arange(0,max(num_vars_pred)+1,step_x)
    yticks = np.arange(0,max(time_pred)+0.1, step_y)
    ax.set_xticks(xticks)
    ax.set_yticks(yticks)
    ax.legend()
    #plt.show()
    name_pic='pictures/'+str(max(num_vars_pred))+'.png'
    name_pic=str(max(num_vars_pred))+'.png'
    fig.savefig(name_pic)
    
    name_vars='results/vars_'+str(max(num_vars_pred))
    name_time='results/time_'+str(max(num_vars_pred))
    np.savetxt(name_vars,num_vars_pred)
    np.savetxt(name_time,time_pred)
   

def pars_time() -> np.array:
    time = np.array([])
    for i in [25, 50, 100, 150, 200, 300, 500, 1000]:
        t = np.loadtxt(f'results/time_{i}')
        time = np.append(time, t)
    return time
