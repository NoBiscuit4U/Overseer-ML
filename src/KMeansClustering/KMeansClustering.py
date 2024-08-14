import numpy as np
import matplotlib.pyplot as plt
import math

class _KMeansClusteringMath:
    #Calculates the distance between two cartesian points
    def EuclideanDistanceFormula(point1,point2):
        return 0.5*((point2[0]-point1[0])**2+(point2[1]-point1[1])**2)

class _KMeansClusteringFuncs:
    def CreatePointArray(xValues,yValues,size):
        pointArray=[]

        for i in range(size):
            pointArray.append([xValues[i],yValues[i]])

        return pointArray
    
    def InitCentroids(pointArray,k):
        kMeansMath=_KMeansClusteringMath
        centroids=[max(pointArray)]
        distancesToAdd=[]
        distances=[]

        if(k>=2 and max(range(len(centroids)))<=2):
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
        
        if(k>2):
            for i in range(k-2):
                print(f"Scalable Generation: {i}")
                sumOfDistances=[]
                centroidDistanceArray=[]
                isAtMax=False
                secondPointIndex=1
                index=0

                while(not isAtMax):
                    centroidDistanceArray.append(kMeansMath.EuclideanDistanceFormula(centroids[index],centroids[secondPointIndex]))

                    if(secondPointIndex+1<len(centroids)):
                        secondPointIndex+=1
                        index+=1
                    else:
                        isAtMax=True
                        #print(f"Centroid Distance to Eachother: {centroidDistanceArray}")

                for point in pointArray:
                    distanceArray=centroidDistanceArray[:]

                    if(point!=any(centroids)):
                        distanceArray.append(kMeansMath.EuclideanDistanceFormula(centroids[secondPointIndex],point))
                        distanceArray.append(kMeansMath.EuclideanDistanceFormula(point,centroids[0]))
                    else:
                        distances.append(0) 
                        
                    distances.append(distanceArray)
                
                for i in range(len(pointArray)):
                    distancesToAdd.append(distances[i])

                    sumOfDistances.append(np.sum(distancesToAdd))
                    distancesToAdd=[]
                
                desiredPoint=max(sumOfDistances)
                print(f"Greatest Perimeter: {desiredPoint}")

                for i in range(len(sumOfDistances)):
                        if(sumOfDistances[i]==desiredPoint):
                            centroids.append(pointArray[i])
                            print(f"New Centroid: {pointArray[i]}")
                
                distances=[]
                sumOfDistances=[]
            return centroids

                    
    def CreateClusterArrays(pointArray,centroids):
        kMeansMath=_KMeansClusteringMath
        centroidGroups=[]

        for centroid in centroids:
            centroidGroups.append([])

        for point in pointArray:
            minDistanceToCentroid=0
            for centroid in centroids:
                newDistanceToCentroid=kMeansMath.EuclideanDistanceFormula(centroid,point)
                
                if(minDistanceToCentroid==0):
                    minDistanceToCentroid=newDistanceToCentroid
                else:
                    if(newDistanceToCentroid<minDistanceToCentroid):
                        minDistanceToCentroid=newDistanceToCentroid

            for i in range(len(centroidGroups)):
                distance=kMeansMath.EuclideanDistanceFormula(centroids[i],point)
                if(minDistanceToCentroid==distance):
                    centroidGroups[i].append(point)
        
        return centroidGroups

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
        self.x=xValues
        self.y=yValues
        self.epochs=epochs
        self.pointArray=kMeansFuncs.CreatePointArray(xValues,yValues,size)
        self.centroids=kMeansFuncs.InitCentroids(self.pointArray,k)
        self.clusterArrays=[]
        print(self.centroids)
    
    def train(self):
        kMeansFuncs=_KMeansClusteringFuncs

        for epoch in range(self.epochs):
            print(f"Epoch: {epoch}")
            if(epoch==0):
                print(f"Starting Centroids: {self.centroids}")
            newCentroids=[]
            clusterArrays=kMeansFuncs.CreateClusterArrays(self.pointArray,self.centroids)
            self.clusterArrays=clusterArrays

            for i in range(len(clusterArrays)):
               newCentroids.append(kMeansFuncs.NewCentroid(clusterArrays[i]))
            
            print(f"New Centroids:{newCentroids}")
            self.centroids=newCentroids

    def plot(self,title,xlabel,ylabel):
            colors=["red","blue","green","cyan","purple","black","white","brown","orange","yellow"]
            for i in range(len(self.clusterArrays)):
                color=colors[i]
                for point in self.clusterArrays[i]:
                    plt.scatter(point[0],point[1],c=color)
            plt.title(title)
            plt.xlabel(xlabel)
            plt.ylabel(ylabel)
            plt.show()
            
        