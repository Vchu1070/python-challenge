import os
import re
import string
from collections import Counter, defaultdict

paragraphtext = os.path.join ('..', 'Resources','Jurassicpark.txt')
with open (paragraphtext, 'r') as text:
    print ("Paragraph Analysis")
    print ("-"*80)
    lines = text.read()
    print (lines)
    print ("-"*80)
    words = lines.split(' ')
    wordcount = len(words)
    print ('Wordcount: '+str(wordcount))
    period = lines.count('.')
    question = lines.count('?')
    exclamation = lines.count('!')
    sentencecount = (period+question+exclamation)
    print ("Approximate Sentence Count: " + str(sentencecount))
    averageword = sum(map(len,words))/len(words)
    print ("Average word length: " +str(averageword))
    averagesentence = (wordcount)/(sentencecount)
    print ("Average sentence length: " + str(averagesentence))