import os
import sqlite3 
import sys

class Manager():
    def __init__(self):
        pass

    def launch_test(self, test, N):
        os.chdir(f'big_test/{test}_test')
        print("in launch\n")
        os.system('pwd')
        signal = os.system(f'python3 new_scr2.py {[N]}') 
        if signal == 0:
            os.chdir('../../')
            return signal  
    
    def visual_test(self, test):
        print("in visual\n")
        os.chdir(f'visual/')
        os.system('pwd')
        signal = os.system(f'python3 {test}_test_hist.py {[N]}')
        if signal == 0:
            os.chdir('../')
            return signal 
   
    def load_to_db(self, test):
        print("in load_to_bd\n")
        os.chdir('db')
        #os.chdir('../db/')
        signal = os.system(f'python3 load.py {test} {[N]}')
        if signal == 0:
            os.chdir('../')
            return signal
        
def clear_DB():
    os.chdir('db/')
    con = sqlite3.connect('data.db')
    cur = con.cursor()
    task = '''DELETE from results'''
    cur.execute(task)
    con.commit()
    cur.close()
    os.chdir('../')

def manage(tests, N):
    os.system('pwd')
    os.system('python3 parse_cpu.py')
    manager = Manager()
    for i in tests:
        manager.launch_test(i, N)
        os.system('pwd')
        manager.visual_test(i)
        os.system('pwd')
        manager.load_to_db(i)
        os.system('pwd')
    
    os.system('cp db/data.db ../../learning_model')
    os.system('echo SUCCESSFUL COMPLETE')
    
    
def get_from_manager(tests, N):
    ind_t = ['1', '2', '3', '4']
    #ind_n= ['25', '50', '100', '150', '200', '300', '500', '1000', '1200']
    out = []
    result_tests = []
    #result_N = []
    for i in ind_t:
        if i in tests:
            result_tests.append(int(i))

    '''for i in ind_n:
        if i in N:
            result_N.append(int(i))
    '''
    return result_tests#, result_N

if __name__ == '__main__':
    tests = list(sys.argv[1])
    N = sys.argv[2]
    print(N)
    tests = get_from_manager(tests, N)
    print(tests, N)
    #tests = [2] debug
    #N = 25 debug
    manage(tests, N)
