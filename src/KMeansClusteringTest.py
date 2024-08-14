import utils.CSVData as csv
import Constants
from KMeansClustering import KMeansClustering as kMC

data=csv.CSVData(Constants.CSVConstants.csvxclaraFP)
xColumn=data.getColumnValues("V1")
yColumn=data.getColumnValues("V2")
newKMeans=kMC.KMeansClustering(2,3,xColumn,yColumn)
newKMeans.train()
newKMeans.plot("Test","x","y")

