def CheckIfIsSymbol(character=""):
    """
    Checks if the inputted character is equal to a symbol.

    Params
    -------------------------------------------------------------------------------
    character: The character you want to compare to a list of symbols.

    -------------------------------------------------------------------------------
    """
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
    """
    Returns a new list of substrings by grouping together characters seperated by a space.

    Params
    -------------------------------------------------------------------------------
    string: The string which you want to pull substrings from.

    -------------------------------------------------------------------------------
    """
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
    """
    Returns a new list of substrings by grouping together characters seperated by a space or forms of punctuation.

    Params
    -------------------------------------------------------------------------------
    string: The string which you want to pull substrings from.

    -------------------------------------------------------------------------------
    """
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

