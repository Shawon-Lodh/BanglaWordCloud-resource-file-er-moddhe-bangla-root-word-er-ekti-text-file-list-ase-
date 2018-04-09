import re
def word_tokenize( string):
    allWords = {}
    totalWordCount = 0;
    sent = re.split('!|\?|\।+|\।\s|০|১|২|৩|৪|৫|৬|৭|৮|৯|=', string)
    #sent = re.sub('[০১২৩৪৫৬৭৮৯]', '', sent2)
    for line in sent:
        line = line.strip()
        words = re.split('\s|,|;|:|-|\.', line)
        for word in words:
            if len(word) > 0:
                totalWordCount += 1;
                if word in allWords:
                    allWords[word] = allWords[word] + 1;
                else:
                    allWords[word] = 1;
        # wordList['wordCount'] = totalWordCount
        # wordList['wordList'] = allWords
    return allWords
