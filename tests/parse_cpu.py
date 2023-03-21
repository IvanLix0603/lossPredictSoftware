import os
import json

def main():
    words = ['Architecture', 'CPU(s)', 'CPU MHz', 'CPU max MHz', 'CPU min MHz', 'L1d cache', 'L1i cache', 'L2 cache', 'L3 cache']
    #words =['Архитектура', 'CPU(s):', 'CPU MHz', 'CPU max MHz', 'CPU min MHz:', 'L1d cache', 'L1i cache', 'L2 cache', 'L3 cache']
     
    os.system('lscpu > lscpuf')
    f = 'lscpuf'
    res = dict()
    for i in range(len(words)):
        res[f'{words[i]}'] = '0,0'
    with open(f, 'r') as f:
           for line in f:
            for i in range(len(words)):
                if words[i] in line:
                    l = line.split(':')[1].replace(' ', '').replace('\n', '')
                    res[f'{words[i]}'] = l   
    
    print(res)

    f = open('cpuinfo.json', 'w')
    json.dump(res, f)
    os.system('rm lscpuf')
    f.close()
    os.system('cp cpuinfo.json db/')
if __name__ == '__main__':
    main()
