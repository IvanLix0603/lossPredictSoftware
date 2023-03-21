from pre_data import launch
from torch import nn
from torch.utils.data import Dataset, DataLoader
from sklearn.model_selection import train_test_split
import torch 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
import torch.optim as optim
import sys
import matplotlib.pyplot as plt

class net(nn.Module):
    def __init__(self, insz):
        super(net, self).__init__()
        self.l13 = nn.Linear(in_features=insz, out_features=26)
        self.lh5 = nn.Linear(in_features=26, out_features=13)
        self.lh2 = nn.Linear(in_features=13, out_features=1)

    def forward(self, inputs):
        out_13 = self.l13(inputs)
        #print(out_13)
        out_relu = torch.relu(out_13)
        #print(out_relu)
        out_5 = self.lh5(out_relu)
        #print(out_5)
        out_relu = torch.sigmoid(out_5)
        #print(out_relu)
        out_2 = self.lh2(out_relu)
        #print(out_2)
        #out_relu = torch.sigmoid(out_2)
        #out_1 = self.lh1(out_relu)
        return torch.relu(out_2)

class perfDataset(Dataset):
    def __init__(self, data):
        x_to_numpy = data.drop(columns='loss').to_numpy()
        y_to_numpy = data['loss'].to_numpy()
        y_to_numpy = y_to_numpy/max(y_to_numpy)
        self.x = torch.from_numpy(x_to_numpy)
        self.y = torch.from_numpy(y_to_numpy)
        self.n_samples = x_to_numpy.shape[0]

    def __getitem__(self, index):
        return self.x[index], self.y[index]

    def __len__(self):
        return self.n_samples


def main():
   data = launch()
   train_set, test_set = train_test_split(data, test_size=0.2)
   type(train_set)
   num_epochs = int(sys.argv[1])
   learning_rate = float(sys.argv[2])
   batch_size = int(sys.argv[3])
  

   trainSet = perfDataset(train_set)
   testSet = perfDataset(test_set)
   train_loader = DataLoader(dataset=trainSet, batch_size=batch_size, shuffle=True)
   test_loader = DataLoader(dataset=testSet,batch_size=batch_size, shuffle=False)
   
   num_epochs_test = int(num_epochs*0.1)
   total_train_samples = len(trainSet)
   total_test_samples = len(testSet)
   
   number_batches_train = math.ceil(total_train_samples/batch_size)
   number_batches_test = math.ceil(total_test_samples/batch_size)


   model = net(13)
   loss = nn.MSELoss()
   optimizer = optim.Adam(model.parameters(), lr=learning_rate)
   
   error_epoch_tr = np.array([])
   error_epoch_ts = np.array([])
   array_epoch = np.array([i for i in range(num_epochs)])
   for epoch in range(num_epochs):
        running_loss = 0
        last_loss = 0
        for i, (inputs, labels) in enumerate(train_loader):
            optimizer.zero_grad()

            outputs = model(inputs.float())
            x_hat = outputs
            loss = ((labels - x_hat.T)**2).sum()
            
            loss.backward()

            optimizer.step()
            running_loss += loss.item()
            if i == 93 and epoch % 10 == 0:
                last_loss = running_loss/number_batches_train
                print("epoch=", epoch, running_loss/number_batches_train)
        error_epoch_tr = np.append(last_loss, error_epoch_tr)
    
   plt.plot(array_epoch, error_epoch_tr)
   plt.grid()
   plt.savefig('Ошибки при обучении')

   for i in range(num_epochs_test):
        running_loss = 0
        last_loss = 0
        with torch.no_grad():
            for i, (inputs, labels) in enumerate(test_loader): 
                inputs = inputs.to(torch.float32) 
                predict = model(inputs) 
                loss = ((labels - predict.T)**2).sum() 
                running_loss+= loss.item()
                print(running_loss/number_batches_test)
                last_loss = running_loss/number_batches_test
        error_epoch_ts = np.append(last_loss, error_epoch_ts)
            

   plt.plot([i for i in range(num_epochs_test)], error_epoch_ts)
   plt.grid()
   plt.savefig('Ошибки при тестировании')
   torch.save(model.state_dict(), 'saved_model')
   

if __name__ == '__main__':
    main()