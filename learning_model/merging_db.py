import sqlite3 as sql3
import pandas as pd
import os


def load(db):
    conn = sql3.connect(db)
    c = conn.cursor()
    c = conn.cursor()
    c.execute('''SELECT * FROM results''')
    df = pd.DataFrame(c.fetchall(), columns = ['Architecture', 'CPU(s)', 'CPU MHz', 'CPU max MHz', 'CPU min MHz', 'L1d cache', 'L1i cache', 'L2 cache', 'L3 cache','hyper_thread', 'N', 'O1', 'O2', 'test_number', 'loss'])
    return df

def main():
    data1 = load(os.path.abspath('data.db'))
    #data2 = load(os.path.abspath('data2.db'))
    data1.to_csv('big_data.csv', mode='a', header=None)
    os.system('rm data.db')
    return 


if __name__ == '__main__':
    main()