import utils.CSVData as csv
import Constants
from LinearRegression import LinearRegression as lr

data=csv.CSVData(Constants.CSVConstants.csvIceCreamPricesFP)
xColumn=data.getColumnValues("Temperature")
yColumn=data.getColumnValues("Ice Cream Profits")
newLR=lr.LinearRegression(500,xColumn,yColumn,366)

newLR.train()
newLR.plot("Temperature Vs. Ice Cream Profits","Temperature","Ice Cream Profits")