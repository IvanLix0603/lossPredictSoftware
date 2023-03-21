import torch 
import pandas as pd
import numpy as np
from torch import nn

class net(nn.Module):
    def __init__(self,  insz=13):
        super(net, self).__init__()
        self.l13 = nn.Linear(in_features=insz, out_features=26)
        self.lh5 = nn.Linear(in_features=26, out_features=13)
        self.lh2 = nn.Linear(in_features=13, out_features=1)
    
    def prepare_data_to_nn(self, data):
        x_to_numpy = data.to_numpy()[0]
        x = torch.from_numpy(x_to_numpy).double()
        return x

    def forward(self, inputs):
        out_13 = self.l13(inputs)
        out_relu = torch.relu(out_13)
        out_5 = self.lh5(out_relu)
        out_relu = torch.sigmoid(out_5)
        out_2 = self.lh2(out_relu)

        return torch.relu(out_2)



        




