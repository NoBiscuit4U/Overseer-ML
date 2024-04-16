import csv

#Class for important universal functions for the main CsvData class
class _CSVFunctions:
    def __init__(self,columns,rows):
        self.columns=columns
        self.rows=rows

    def columnValues(self,targetColumn=""):
        output=[]
        i=0

        for column in self.columns:
            if(targetColumn==column):
                for row in self.rows:
                    if(row!=self.rows[0]):
                        output.append(float(row[i])) 
            else:
                i+=1
        
        return output

#The main class for processing information from a csv
class CSVData:
    def __init__(self,csvFile):
        with open(csvFile) as f:
            reader=list(csv.reader(f))
            rows=reader.copy()

        self.rows=rows
        self.columns=rows[0]
        self.rowCount=len(rows)
        self.columnCount=len(rows[0])
    
        self.csvFuncs=_CSVFunctions(self.columns,self.rows)

        #print(self.columns)
        #for row in self.rows:
            #if row!=self.rows[0]:
               #print(row)
        #print(self.rowCount)
        #print(self.columnCount)

    def getColumnValues(self,targetColumn):
        return self.csvFuncs.columnValues(targetColumn)
    
    #Function to find unique values in a column
    def findUnique(self,targetColumn=""):
        uniqueValues=[]
        values=[]
        i=0

        values=self.csvFuncs.columnValues(targetColumn)

        for value in values:
            for i in range(len(values)):
                if(value==values[i]):
                    if(len(uniqueValues)==0):
                        uniqueValues.append(value)
                    else:
                        if values[i] not in uniqueValues:
                            uniqueValues.append(value)

        #print(uniqueValues)
        return uniqueValues

    #Function to OneHotEncode a specific column
    #OneHotEncoding is an inefficent way to encode data for certain use cases
    def oneHotEncode(self,uniqueValues,targetColumn=""):
        outputMatrix=[]
        values=[]
        i=0

        values=self.csvFuncs.columnValues(targetColumn)

        for value in values:
            newMatrixRow=[]

            for i in range(len(uniqueValues)):
                if(value==uniqueValues[i]):
                    newMatrixRow.append(1)
                else:
                    newMatrixRow.append(0)

                if i==max(range(len(uniqueValues))):
                    outputMatrix.append(newMatrixRow)

        #print(uniqueTokens)
        #for row in outputMatrix:
        #    print(row)
        return outputMatrix
    