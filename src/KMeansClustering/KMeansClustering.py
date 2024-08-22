import numpy as np
import matplotlib.pyplot as plt
import math

class _KMeansClusteringMath:
    #Calculates the distance between two cartesian points
    def EuclideanDistanceFormula(n1,n2):
        return 0.5*((n2[0]-n1[0])**2+(n2[1]-n1[1])**2)

    #Returns a normalized set of data
    #Set of data within a range of 0-1 that contains the same variation as the previous values
    def Normalize(data):
        min=np.amin(data)
        range=np.amax(data)-min
        return np.array((data-min)/range)

class _KMeansClusteringFuncs:
    def CreatePointArray(x,y,size):
        pointArray=[]

        for i in range(size):
            pointArray.append([x[i],y[i]])

        return pointArray
    
    def InitCentroids(nArray,k):
        kMeansMath=_KMeansClusteringMath
        c=[max(nArray)]
        disAdd=[]
        dis=[]

        if(k>=2 and max(range(len(c)))<=2):
            for n in nArray:
                if(n!=any(c)):
                    dis.append(kMeansMath.EuclideanDistanceFormula(c[0],n))
                else:
                    dis.append(0) 
            
            c1=np.amax(dis)

            for i in range(len(nArray)):
                if(dis[i]==c1):
                    c.append(nArray[i])
            
            dis=[]
        
        if(k>2):
            for i in range(k-2):
                print(f"Scalable Generation: {i}")
                disSumm=[]
                cDis=[]
                isFinal=False
                i1=0
                i2=1

                while(not isFinal):
                    cDis.append(kMeansMath.EuclideanDistanceFormula(c[i],c[i2]))

                    if(i2+1<len(c)):
                        i2+=1
                        i1+=1
                    else:
                        isFinal=True
                        #print(f"Centroid Distance to Eachother: {cDis}")

                for n in nArray:
                    t_dis=cDis[:]

                    if(n!=any(c)):
                        t_dis.append(kMeansMath.EuclideanDistanceFormula(c[i2],n))
                        t_dis.append(kMeansMath.EuclideanDistanceFormula(n,c[0]))
                    else:
                        dis.append(0) 
                        
                    dis.append(t_dis)
                
                for i in range(len(nArray)):
                    disAdd.append(dis[i])

                    disSumm.append(np.sum(disAdd))
                    disAdd=[]
                
                desiredn=max(disSumm)
                print(f"Greatest Perimeter: {desiredn}")

                for i in range(len(disSumm)):
                        if(disSumm[i]==desiredn):
                            c.append(nArray[i])
                            print(f"New Centroid: {nArray[i]}")
                
                dis=[]
                disSumm=[]
            return c

                    
    def CreateClusterArrays(nArray,centroids):
        kMeansMath=_KMeansClusteringMath
        k=[]

        for c in centroids:
            k.append([])

        for n in nArray:
            minDis=0
            for c in centroids:
                newDis=kMeansMath.EuclideanDistanceFormula(c,n)
                
                if(minDis==0):
                    minDis=newDis
                else:
                    if(newDis<minDis):
                        minDis=newDis
  
            for i in range(len(k)):
                dis=kMeansMath.EuclideanDistanceFormula(centroids[i],n)
                if(minDis==dis):
                    k[i].append(n)
   
        return k

    def NewCentroid(nArray=[[0,0]]):
        ycoords=[]
        xcoords=[]
        for n in nArray:
            xcoords.append(n[0])
            ycoords.append(n[1])

        meanx=np.mean(xcoords)
        meany=np.mean(ycoords)
        return [meanx,meany]
    
    def SilhouetteScore(avinter,avintra):
        return (avintra-avinter)/max(avinter,avintra)

class KMeansClustering:
    def __init__(self,epochs,k,xValues,yValues,size=0):
        kMeansFuncs=_KMeansClusteringFuncs
        if(size==0):
            size=len(xValues)
        self.x=xValues
        self.y=yValues
        self.epochs=epochs
        self.nArray=kMeansFuncs.CreatePointArray(xValues,yValues,size)
        self.centroids=kMeansFuncs.InitCentroids(self.nArray,k)
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
            
        