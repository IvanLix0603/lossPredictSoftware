import os
import sys

def main(N):
    for i  in  N:
        print(i)
        os.system(f'bash scr1.sh {i}')
   
def get_from_manager(N):
    ind = ['25', '50', '100', '150', '200']
    out = []
    result_N = []
    for i in ind:
        if i in N:
            result_N.append(int(i))
    return result_N

if __name__ == '__main__':
    N = sys.argv[1] 
    N = get_from_manager(N)
    main(N)
    os.system('cp  -r results/* ../../visual/2_test')    
