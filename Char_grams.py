# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 00:08:10 2021

@author: Aditi.Dhamat
"""
import nltk
import numpy as np
import random

text = """Global warming or climate change has become a worldwide concern.It is a concern and is causing melting glaciers,changing weather patterns, rising sea levels, floods, cyclones and droughts. Global warming implies an increase in the average temperature of the Earth due to entrapment of greenhouse gases in the earth's atmosphere."""
n = 6 #tri grams

ngrams = {}
#Create the n-grams
for i in range(len(text)-n):
    gram = text[i:i+n]  #text[0:3] = Glo - at start 
    if gram not in ngrams.keys():
        ngrams[gram] = []
    ngrams[gram].append(text[i+n]) #text[0+3] = text[3] = b
 
#Testing N-gram model
currentGram = text[0:n]
result = currentGram

for i in range(100):
    if currentGram not in ngrams.keys():
        break
    possibilities = ngrams[currentGram]
    nextItem = possibilities[random.randrange(len(possibilities))]
    result += nextItem
    currentGram = result[len(result)-n:len(result)]

print(result)
