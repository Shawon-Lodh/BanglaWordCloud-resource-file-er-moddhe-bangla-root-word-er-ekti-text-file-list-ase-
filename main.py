import codecs
from os import path
from tokenizer import tokenize
from word_tokenize_bn import *
from stemmer import *

import numpy as np
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from quadtree import *
from utils import *

lan_bn = [ '০১২৩৪৫৬৭৮৯', ',.;:!?-', 'অআইঈউঊএঐওঔকখগঘঙচছজঝঞটঠডঢণতথদধনপফবভমযরলশষসহড়ঢ়য়ৎ‌়◌াি◌ী◌ু◌ূ◌ৃেৈোৌ◌্' ]

d = path.dirname(__file__)

def process_text(text):
    wordsList = word_tokenize(text)
    words = {}

    for word in wordsList:
        # remove stopwords
        if word not in stopwords:
            # print('adding word ' + word)
            words[word] = wordsList[word]
        # else:
        #     print('deleting ' + word)
        #print('stem of '+word +' is ' +findStem(word))
    # print(len(wordsList))
    # print(len(words))
    print(sorted(words.items(), key=lambda kv: kv[1], reverse=True))
    finalListWord = dict()
    for word in words:
        stemWord = findStem(word)
        if stemWord in finalListWord:
            finalListWord[stemWord] = finalListWord[stemWord] + words[word]
        else:
            finalListWord[stemWord] = words[word]
    sortedList = sorted(finalListWord.items(), key=lambda kv: kv[1], reverse=True)
    #print(sortedList)
    # for word in sortedList:
    #     print(word[1] ,word[0])
    # return sortedList
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

wordList = process_text(text)
draw_text(wordList)

# process words
# import numpy as np
# from PIL import Image
# from PIL import ImageFont
# from PIL import ImageDraw
# # Image size
# width = 600
# height = 300
# channels = 3
#
# # Create an empty image
# #img = np.zeros((height, width, channels), dtype=np.uint8)
# img = Image.new('RGB', (width, height), color = 'white')
# img.save('test.jpg')
# img = Image.open('test.jpg')
# draw = ImageDraw.Draw(img)
# font = ImageFont.truetype("C:\Windows\Fonts\Siyamrupali.ttf", 40, encoding="utf-8")
# text = u"ফসল"
# #.encode('UTF-8')
# w, h = font.getsize(text)
# draw.text(((width-w)/2,(height-h)/2), text , 'red',font=font)
# img.save('test.jpg')
#
#
#
#
#
#
