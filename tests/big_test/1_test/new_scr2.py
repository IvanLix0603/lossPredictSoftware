import os
import sys
from predict_1200 import main_1200

def main(N):
    N = get_from_manager(N)
    for i  in  N:
        os.system(f'bash scr1.sh {i}')
    if 1000 in N:
        main_1200(N)

    

def get_from_manager(N):
    ind = ['25', '50', '100', '150', '200', '300', '500', '1000', '1200']
    result_N = []
    for i in ind:
        if i in N:
            result_N.append(int(i))
    return result_N

if __name__ == '__main__':
    N = sys.argv[1]
    print('in new_scr=',N) 
    main(N)
    os.system('cp  -r results/* ../../visual/1_test')