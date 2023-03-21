import numpy as np
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

class PolyPredict():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def predict(self, f1200=False):
        #shape_data = self.x.shape[0]
        xfit = np.arange(2,max(self.x))
        poly_model = make_pipeline(PolynomialFeatures(3), LinearRegression())
        poly_model.fit(self.x[:, np.newaxis], self.y)
        ypred = 0
        xpred = np.arange(2, 1201)    
        if f1200 == True:
            #xpred = np.linspace(0,1200,shape_data)    
            ypred = poly_model.predict(xpred[:, np.newaxis])
            return ypred, xpred
        else:
            ypred = poly_model.predict(xfit[:, np.newaxis])   
            return ypred
