import os

class launchTests():
    def __init__(self, tests, N):
        tests = str(tests)
        N = str(N)
        os.chdir('tests')
        os.system(f'python3 main.py {[tests]} {[N]}')
        os.chdir('../')

