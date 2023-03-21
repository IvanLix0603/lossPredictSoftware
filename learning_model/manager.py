import os

class launchLearnig():
    def __init__(self, nE, lR, bS): #######
        os.chdir('learning_model')
        os.system('cp ../tests/db/data.db .')
        print('Status: db copied from tests')
        os.system('python3 merging_db.py')
        print('Status: db merged')
        os.system(f'python3 nn.py {nE} {lR} {bS}')
        os.system('cp saved_model ../applicatedNN')
        print('Status: model copied')
        os.chdir('../')
        