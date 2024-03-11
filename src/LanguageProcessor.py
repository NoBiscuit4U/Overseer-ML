import Tokenizer as token
from Constants import LanguageProcessorConstants as lpcons
import nltk
import csv
import os

def appendTokensToCSV(csvFP,string):
    #appends string value to csv file
    #for i in  
    tokens=token.SpaceTokenizer(string)

    with open(csvFP,"a") as fp:
        csvWriter=csv.writer(fp)
        csvWriter.writerow(tokens)

