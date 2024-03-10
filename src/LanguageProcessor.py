from nltk import SpaceTokenizer as sTokenizer
from Constants import LanguageProcessorConstants as lpcons
import nltk
import csv
import os

def tokenizeString(**string):
    #Tokenizes a string 
    tokenizer=sTokenizer
    
    tokens=tokenizer.tokenize(tokenizer,string)

    print(tokens)
    return tokens

def appendTokensToCSV(csvFP,string):
    #appends string value to csv file
    #for i in  
    tokens=tokenizeString(string)

    with open(csvFP,"a") as fp:
        csvWriter=csv.writer(fp)
        csvWriter.writerow(tokens)

appendTokensToCSV(lpcons.csvFP,"I AM A BIRD")