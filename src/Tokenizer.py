import os

def SpaceTokenizer(string=""):
    strLength=range(len(string))
    outputList=[]
    lastpos=0
    
    for i in strLength:
        if(string[i]==" "):
            characters=string[0+lastpos:i]    
            outputList.append(characters) 
            lastpos=i+1
        else:
            if(i==max(strLength)):
                characters=string[0+lastpos:i+1]    
                outputList.append(characters) 
            i+=1
    
    return outputList

