import os
from threading import Thread
import time 
import sys
from predict_1200 import main_1200



class launch_4test():
    def __init__(self):
        self.N = N
        self.main()
        pass

    def test(self): 
        for i  in  N:
            os.system(f'bash scr1.sh {i}')
        if 1000 in N:
            main_1200(N)

    def backup(self):
        os.system('yes > /dev/null 2>&1 &')


    def main(self):
        Thread(target=self.test).start()
        Thread(target=self.backup).start()


    def get_from_manager(self, N):
        ind = ['25', '50', '100', '150', '200', '300', '500', '1000', '1200']
        result_N = []
        for i in ind:
            if i in N:
                result_N.append(int(i))
        return result_N


if __name__ == '__main__':
    N = sys.argv[1]
    l = launch_4test() 
    N = l.get_from_manager(N)
    l.main()
    os.system('cp  -r results/* ../../visual/4_test')
    os.system('echo copied data')