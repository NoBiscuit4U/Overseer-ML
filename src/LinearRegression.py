import numpy as np

class LinearRegression:
    def __init__(self):
        self.m=0
        self.b=0

    def forward_prop(self,input): 
        predictions=np.multiply(self.m,input)+self.b
        return predictions
    