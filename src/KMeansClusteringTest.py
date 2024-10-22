import utils.CSVData as csv
import Constants
from KMeansClustering import KMeansClustering as kMC

#data=csv.CSVData(Constants.CSVConstants.csvxclaraFP)
data=csv.CSVData(Constants.CSVConstants.csvcalHousing)
xColumn=data.getColumnValues("longitude")
yColumn=data.getColumnValues("latitude")
newKMeans=kMC.KMeansClustering(2,5,xColumn,yColumn)
newKMeans.train()
newKMeans.plot("Lon vs. Lat","Longitude","Latitude")
#newKMeans.elbow()

