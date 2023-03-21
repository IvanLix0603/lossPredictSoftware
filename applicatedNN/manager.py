from applicatedNN.neuralnet import net
import torch

class launchPredict():
    def __init__(self):
        #self.window.exit.clicked.connect(app.quit)
        self.model = net()
    
    def predict(self, data):
        print(data)
        self.model.state_dict(torch.load('applicatedNN/saved_model'))
        inputs = self.model.prepare_data_to_nn(data)
        inputs = inputs.type(torch.float32)
        result = self.model.forward(inputs)
        result = round(result.tolist()[0], 4)
        result = str(result)
        return result
        
    


