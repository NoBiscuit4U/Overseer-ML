import numpy as np
import matplotlib.pyplot as plt
import math

class _KMeansClusteringMath:
    def EuclideanDistanceFormula(point1,point2):
        return 0.5*((abs(point2[0]-point1[0]))**2+(abs(point2[1]-point1[1]))**2)

class _KMeansClusteringFuncs:
    def CreatePointArray(xValues,yValues,size):
        pointArray=[]

        for i in range(size):
            pointArray.append([xValues[i],yValues[i]])

        return pointArray
    
    def InitCentroids(pointArray,k):
        kMeansMath=_KMeansClusteringMath
        centroids=[pointArray[np.random.randint(0,len(pointArray))]]
        distancesToAdd=[]
        distances=[]

        if(k>=2):
            for point in pointArray:
                if(point!=any(centroids)):
                    distances.append(kMeansMath.EuclideanDistanceFormula(centroids[0],point))
                else:
                    distances.append(0) 
            
            desiredPoint=np.amax(distances)

            for i in range(len(pointArray)):
                if(distances[i]==desiredPoint):
                    centroids.append(pointArray[i])
            
            distances=[]
        
        while(k-1!=max(range(len(centroids))) and max(range(len(centroids)))>=2):
            sumOfDistances=[]

            for centroid in centroids:
                distanceArray=[]

                for point in pointArray:
                    if(point!=any(centroids)):
                        distanceArray.append(kMeansMath.EuclideanDistanceFormula(centroid,point))
                    else:
                        distances.append(0) 
            
                distances.append(distanceArray)
            
            for i in range(len(pointArray)):
                for distanceArray in distances:
                    distancesToAdd.append(distanceArray[i])

                sumOfDistances.append(np.sum(distancesToAdd))
                distancesToAdd=[]
            
            desiredPoint=np.amax(sumOfDistances)

            for i in range(len(sumOfDistances)):
                if(sumOfDistances[i]==desiredPoint):
                    centroids.append(pointArray[i])
            
            distances=[]
        return centroids

                    
    #def CreateClusterArrays(pointArray,centroids):

    def NewCentroid(pointArray=[[0,0]]):
        ycoords=[]
        xcoords=[]
        for point in pointArray:
            xcoords.append(point[0])
            ycoords.append(point[1])

        meanx=np.mean(xcoords)
        meany=np.mean(ycoords)
        return [meanx,meany]

class KMeansClustering:
    def __init__(self,epochs,k,xValues,yValues,size=0):
        kMeansFuncs=_KMeansClusteringFuncs
        if(size==0):
            size=len(xValues)
        self.epochs=epochs
        self.pointArray=kMeansFuncs.CreatePointArray(xValues,yValues,size)
        self.clusterArrays=[]
        self.centroids=kMeansFuncs.InitCentroids(self.pointArray,k)
        print(self.centroids)
    
    def train(self):
        kMeansFuncs=_KMeansClusteringFuncs

        #for epoch in range(self.epochs):

            
        