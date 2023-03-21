#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

class PolyPredict():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def predict(self):
        shape_data = self.x.shape[0]
        #print(shape_data)
        xfit = np.linspace(0,max(self.x),shape_data)
        
        poly_model = make_pipeline(PolynomialFeatures(3), LinearRegression())
        
        poly_model.fit(self.x[:, np.newaxis], self.y)
        ypred = poly_model.predict(xfit[:, np.newaxis])
        
#        plt.scatter(self.x, self.y)
#        plt.plot(xfit, ypred)
#       plt.grid()
#        plt.show()            
    
        return ypred
