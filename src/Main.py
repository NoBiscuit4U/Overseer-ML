import CSVData as csv
import Constants
from LinearRegression import LinearRegression as lr

data=csv.CSVData(Constants.CSVConstants.csvStockPricesFP)
xColumn=data.ColumnValues(0)
yColumn=data.ColumnValues(1)
newLR=lr.LinearRegression(50,xColumn,yColumn,366)

newLR.train()