def CheckIfIsSymbol(character=""):
    listOfSymbols=[".",",","?","#","!","@","$","%","<",
                   ">",":",";","'",'"',"{","}","[","]",
                   "=","-","_","+","*","(",")","&","^"]
    listLen=range(len(listOfSymbols))

    for s in listLen:
        if(listOfSymbols[s]==character):
            return True
        else:
            if(s==max(listLen)):
                return False         

def SpaceTokenizer(string=""):
    strLen=range(len(string))
    outputList=[]
    lastpos=0
    
    for i in strLen:
        if(string[i]==" "):
            characters=string[lastpos:i]    
            outputList.append(characters) 
            lastpos=i+1
        else:
            if(i==max(strLen)):
                characters=string[lastpos:i+1]    
                outputList.append(characters) 

    return outputList

def PunctuationTokenizer(string=""):
    strLen=range(len(string))
    outputList=[]
    newList=[]
    lastpos=0

    for i in strLen:
        if(string[i]==" " or CheckIfIsSymbol(string[i])):
            if(CheckIfIsSymbol(string[i])):
                symbol=string[i]
                characters=string[lastpos:i]    
                newList.append(characters) 
                newList.append(symbol)
                lastpos=i+1
            else:
                characters=string[lastpos:i]    
                newList.append(characters) 
                lastpos=i+1

        else:
            if(i==max(strLen)):
                characters=string[lastpos:i+1]    
                newList.append(characters) 
    
    for i in range(len(newList)):
        if(newList[i]!=""):
            outputList.append(newList[i])
        
        i+=1

    return outputList

