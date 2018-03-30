import codecs
from os import path
from tokenizer import tokenize
from word_tokenize_bn import *
from stemmer import *


lan_bn = [ '০১২৩৪৫৬৭৮৯', ',.;:!?-', 'অআইঈউঊএঐওঔকখগঘঙচছজঝঞটঠডঢণতথদধনপফবভমযরলশষসহড়ঢ়য়ৎ‌়◌াি◌ী◌ু◌ূ◌ৃেৈোৌ◌্' ]

d = path.dirname(__file__)

def process_text(text):
    wordsList = word_tokenize(text)
    words = {}

    # remove stopwords
    #words = [word for word in words if word not in stopwords]
    for word in wordsList:
        # remove number
        if word is not word.isdigit():
            # remove stopwords
            if word not in stopwords:
                # print('adding word ' + word)
                words[word] = wordsList[word]
            # else:
            #     print('deleting ' + word)
        # else:
        #     print('deleting number'+ word)
        #print('stem of '+word +' is ' +findStem(word))
    # print(len(wordsList))
    # print(len(words))
    finalListWord = dict()
    for word in words:
        stemWord = findStem(word)
        if stemWord in finalListWord:
            finalListWord[stemWord] = finalListWord[stemWord] + words[word]
        else:
            finalListWord[stemWord] = words[word]

    # print(finalListWord)
    # print(words)
    # print(len(finalListWord))

    #remove number
    #words = [word for word in words if not word.isdigit()]

stopwords = open(d+ '/resources/stopwords-bn.txt', encoding='utf-8').read()
#print(stopwords)
text = open(d + '/resources/islamic3_bn.txt', encoding='utf-8').read()
tokens = tokenize(text, lan_bn)

rootFilePath = d+'/resources/RootFile.txt'
stemmedWords = loadStemmedWords(rootFilePath)

process_text(text)

# process words







