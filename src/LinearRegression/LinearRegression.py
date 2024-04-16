import numpy as np
import matplotlib.pyplot as plt

class _LinearRegressionMath:
        #Sum Squared Error Function
    def SSE(y,pred):
        return 0.5*np.sum((y-pred)**2)

        #Returns the Derivative of a Weight
    def GetWeightDerivative(y,pred,x):
        return np.sum(-(y-pred)*x)

        #Returns the Last Output
        #Using Weight1, Weight0, Bias, and the Input
    def GetLastOutput(w0,x0,w1,x1):
        return w0*x0+w1*x1

        #Returns the Standard Deviation of the Input
    def StandardDeviation(data,mean):
        summation=np.sum((mean-data)**2)
        return (summation/len(data))**0.5
    
        #Returns a normalized set of data
        #Set of data within a range of 0-1 that contains the same variation
    def Normalize(data):
        min=np.amin(data)
        range=np.amax(data)-min
        return np.array((data-min)/range)
        

class LinearRegression:
    def __init__(self,epochs,xValues,yValues,size,learnRate=0.001,bias=1):
        lrMath=_LinearRegressionMath
        #Bias
        self.x0=bias
        #Weights (Randomly Assign Starting Weights)
        self.w0=np.random.uniform(-2,1,size=1)
        self.w1=np.random.uniform(2,3,size=1)
        #x-values
        self.xVals=np.array(xValues[0:size])
        #y-values
        self.yVals=np.array(yValues[0:size])
        #Normalized x-values
        self.x1=lrMath.Normalize(self.xVals)
        #Normalized y-values
        self.y=lrMath.Normalize(self.yVals)
        #Learning rate
        self.learnRate=learnRate
        #Epochs
        self.epochs=epochs

    def train(self):
        lrMath=_LinearRegressionMath
        
        for epoch in range(self.epochs):
                pred=lrMath.GetLastOutput(self.w0,self.x0,self.w1,self.x1)
                error=lrMath.SSE(self.y,pred)
                derivw0=lrMath.GetWeightDerivative(self.y,pred,self.x0)
                derivw1=lrMath.GetWeightDerivative(self.y,pred,self.x1)
                self.w0=self.w0-self.learnRate*derivw0
                self.w1=self.w1-self.learnRate*derivw1
                print(f"Deriv0: {derivw0} Deriv1: {derivw1}")
                print(f"w0: {self.w0} w1: {self.w1}")
                print(f"Current Epoch: {epoch} Error: {error}")
        
    def plot(self,title,xlabel,ylabel):
        lrMath=_LinearRegressionMath

        lrPred=lrMath.GetLastOutput(self.w0,self.x0,self.w1,self.x1)
        plt.scatter(self.x1,self.y)
        plt.plot(self.x1,lrPred)
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.show()
                