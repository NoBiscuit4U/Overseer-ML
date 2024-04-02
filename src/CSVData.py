import csv

class CSVData:
    def __new__(cls,*args,**kargs):
        return super().__new__(cls)
    
    def __init__(self,csvFile):
        self.csvFile=csvFile
    
        with open(csvFile) as f:
            reader=list(csv.reader(f))
            rows=reader.copy()

        self.rows=rows
        self.columns=rows[0]
        self.rowCount=len(rows)
        self.columnCount=len(rows[0])
        #print(self.columns)
        #for row in self.rows:
            #if row!=self.rows[0]:
               #print(row)
        #print(self.rowCount)
        #print(self.columnCount)
    
    def findUnique(self,targetColumn):
        outputTokens=[]
        tokens=[]

        for row in self.rows:
                if(row!=self.rows[0]):
                    tokens.append(row[targetColumn])

        for token in tokens:
            for i in range(len(tokens)):
                if(token==tokens[i]):
                    if(len(outputTokens)==0):
                        outputTokens.append(token)
                    else:
                        if tokens[i] not in outputTokens:
                            outputTokens.append(token)

        #print(outputTokens)
        return outputTokens


    def oneHotEncode(self,uniqueTokens,targetColumn):
        outputMatrix=[]
        tokens=[]

        uniqueTokens=uniqueTokens

        for row in self.rows:
            if(row!=self.rows[0]):
                for element in row:
                    if(element==row[targetColumn]):
                        tokens.append(element)

        for token in tokens:
            newMatrixRow=[]

            for i in range(len(uniqueTokens)):
                if(token==uniqueTokens[i]):
                    newMatrixRow.append(1)
                else:
                    newMatrixRow.append(0)

                if i==max(range(len(uniqueTokens))):
                    outputMatrix.append(newMatrixRow)

        #print(uniqueTokens)
        #for row in outputMatrix:
        #    print(row)
        return outputMatrix

data=CSVData("c:/VS/SpeechMimicry/src/worddatabase.csv")
    