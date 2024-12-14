import numpy as np
import matplotlib.pyplot as plt

class _LinearRegressionMath:
    
        #Returns a normalized set of data
        #Set of data within a range of 0-1 that contains the same variation as the previous values
    def Normalize(data):
        min=np.amin(data)
        range=np.amax(data)-min
        return np.array((data-min)/range)

        

class LinearRegression:
    """
        Instantiates a new linear regression model. Linear regression is used to find the line of best fit,
        which is used to find and visualize a correlation between an independent and dependent variable.

        Params
        -------------------------------------------------------------------------------
        - epochs: The number of iterations the model will run through.
        
        - xValues: The dependent variable used on the x-axis.

        - yValues: The independent variable used on the y-axis.

        - size: The desired number of values from the x and yValue arrays.

        - learningRate: The rate at which the model tries to go to the desired error. (If the number is too low it will take a long time, if it is to high it will overshoot and oscillate)
    
        - bias: Can be used to change the desired slope of the line.
        -------------------------------------------------------------------------------

        Funcs
        -------------------------------------------------------------------------------
        - train: Runs the model for the desired epochs and prints the derivatives, the weights, and the current epoch to the terminal.

        - plot: Plots the line of best fit and shows variation off the line
        -------------------------------------------------------------------------------
    """
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
        
    def plot(self,title,xlabel,ylabel):
        lrMath=_LinearRegressionMath
