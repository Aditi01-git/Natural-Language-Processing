# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 01:45:37 2021

@author: Aditi.Dhamat
"""

import regex as re
import nltk 
import heapq
import numpy as np

paragraph = """Thank you all so very much. 
                Thank you to the Academy. Thank you to all of you in
                this room. I have to congratulate the other
                incredible nominees this year. The Revenant was the
                product of the tireless efforts of an unbelievable 
                cast and crew. First off, to my brother in this 
                endeavor, Mr. Tom Hardy. Tom, your talent on screen 
                can only be surpassed by your friendship off screen.
                Thank you for creating a transcendent cinematic experience. 
                Thank you to everybody at Fox and New Regency … 
                my entire team. I have to thank everyone from the 
                very onset of my career … To my parents; none of this 
                would be possible without you. And to my friends, 
                I love you dearly; you know who you are.And lastly, 
                I just want to say this: Making The Revenant was 
                about man's relationship to the natural world. 
                A world that we collectively felt in 2015 as the 
                hottest year in recorded history. Our production 
                needed to move to the southern tip of this planet 
                just to be able to find snow. Climate change is real, 
                it is happening right now. It is the most urgent 
                threat facing our entire species, and we need to work 
                collectively together and stop procrastinating. We 
                need to support leaders around the world who do not 
                speak for the big polluters, but who speak for all of 
                humanity, for the indigenous people of the world, for 
                the billions and billions of underprivileged people 
                out there who would be most affected by this. For our 
                children’s children, and for those people out there 
                whose voices have been drowned out by the politics of 
                greed. I thank you all for this amazing award tonight.
                Let us not take this planet for granted. I do not 
                take tonight for granted. Thank you so very much."""
                
sentences = nltk.sent_tokenize(paragraph)

for i in range(len(sentences)):
    sentences[i] = sentences[i].lower()
    sentences[i] = re.sub(r"\W", " ", sentences[i])
    sentences[i] = re.sub(r"\s+", " ", sentences[i])
    
#Create a histogram
wordcount = {}
for data in sentences:
    words = nltk.word_tokenize(data)
    for word in words:
        if word not in wordcount.keys():
            wordcount[word] = 1
        else:
            wordcount[word] += 1

                
freq_words = heapq.nlargest(100, wordcount, key=wordcount.get)

#IDF for each word
word_idf = {}

for word in freq_words:
    doc_count = 0
    for data in sentences:
        if word in nltk.word_tokenize(data):
            doc_count += 1
    word_idf[word] = np.log((len(sentences)/doc_count)+1) #+1 for bias
    
#TF for each word in each document
tf_matrix = {}

for word in freq_words:
    doc_tf = []
    for data in sentences:
        freq = 0
        for w in nltk.word_tokenize(data):
            if w == word:
                freq += 1 
        tf_word = freq / len(nltk.word_tokenize(data))
        doc_tf.append(tf_word)
    tf_matrix[word] = doc_tf

#TF-IDF

tfidf_matrix = []

for word in tf_matrix.keys():
    tfidf = []
    for value in tf_matrix[word]:
        score = value * word_idf[word]
        tfidf.append(score)
    tfidf_matrix.append(tfidf)
    
X = np.asarray(tfidf_matrix)
X = np.transpose(X)
    