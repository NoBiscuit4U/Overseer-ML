import numpy as np
#import matplotlib.pyplot as plt

class LinearRegressionMath:
        #Sum Squared Error Function
    def SSE(y,pred):
        return 0.50*np.sum((y-pred)**2)

        #Returns the Derivative of a Weight
    def GetWeightDerivative(y,pred,w):
        return np.sum(-(y-pred)*w)

        #Returns the Output Of the Node
    def GetLastOutput(w0,x0,w1,x1):
        return w1*x1+w0*x0

        #Returns the Standard Deviation of the Input
    def StandardDeviation(data,mean):
        summation=np.sum((mean-data)**2)
        return (summation/len(data))**0.5

class LinearRegression:
    def __init__(self,epochs,xValues,yValues,size,learnRate=0.001,bias=1):
        lrMath=LinearRegressionMath
        #Bias
        self.x0=bias
        #Weights (Randomly Assign Starting Weights)
        self.w0=np.random.uniform(-2,1,size=1)
        self.w1=np.random.uniform(2,3,size=1)
        #X-values
        self.x1=np.array(xValues[0:size])
        #print(self.x1)
        #Y-values
        self.y=np.array(yValues[0:size])
        #print(self.y)
        #Learning rate
        self.learnRate=learnRate
        #Epochs
        self.epochs=epochs

    def train(self):
        lrMath=LinearRegressionMath
        
        for epoch in range(self.epochs):
                pred=lrMath.GetLastOutput(self.w0,self.x0,self.w1,self.x1)
                error=lrMath.SSE(self.y,pred)
                derivw0=lrMath.GetWeightDerivative(self.y,pred,self.x0)
                derivw1=lrMath.GetWeightDerivative(self.y,pred,self.x1)
                print(f"Deriv1: {derivw0} Deriv2: {derivw1}")
                self.w0=self.w0-self.learnRate*derivw0
                self.w1=self.w1-self.learnRate*derivw1
                print(f"w0: {self.w0} w1: {self.w1}")
                print(f"Current Epoch: {epoch} Error: {error}")
        
    def plot(self):
        lrMath=LinearRegressionMath

        lrPred=lrMath.GetLastOutput(self.w0,self.x0,self.w1,self.x1)
        #plt.scatter(self.x1,self.y)
        #plt.plot(self.x1,lrPred)
        #plt.show()
                