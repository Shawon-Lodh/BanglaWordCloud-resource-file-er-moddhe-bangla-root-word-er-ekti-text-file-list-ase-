from os import path
from collections import defaultdict

stemmeWords = defaultdict(dict)
def loadStemmedWords(path):
    rootFile = open(path, encoding='utf-8')
    lines = rootFile.readlines()

    stemmed = ""
    beforeStem = ""
    status = 0
    for inputLine in lines:
        line =  inputLine.strip()
        if len(line) > 0:
            if line.endswith("*"):
                if status is 1:
                    if stemmed not in stemmeWords:
                        stemmeWords[stemmed] = stemmed
                stemmed = line[:-2]
                status = 1
            elif line == "-----------------------------------" :
                continue
            else:
                beforeStem = line
                if beforeStem not in stemmeWords:
                    stemmeWords[beforeStem] = stemmed
    return stemmeWords
def findStem(termToStem):
    if termToStem in stemmeWords:
        return  stemmeWords[termToStem]
    return termToStem
# d = path.dirname(__file__)
# rootFilePath = d+'/resources/RootFile.txt'
# words = loadStemmedWords(rootFilePath)
# print(stemmeWords)
# print(findStem('অংকটাও'))