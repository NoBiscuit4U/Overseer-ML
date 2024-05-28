import utils.CSVData as csv
import Constants
from KMeansClustering import KMeansClustering as kMC

data=csv.CSVData(Constants.CSVConstants.csvIceCreamPricesFP)
xColumn=data.getColumnValues("Temperature")
yColumn=data.getColumnValues("Ice Cream Profits")
newKMeans=kMC.KMeansClustering(500,3,xColumn,yColumn)
