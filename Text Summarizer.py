# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 15:46:23 2021

@author: Aditi.Dhamat
"""

import bs4 as bs
import urllib.request
import re
import nltk
import heapq


#Getting the data(Scraping- parsing articles)
source = urllib.request.urlopen("https://en.wikipedia.org/wiki/Climate_change").read()

soup = bs.BeautifulSoup(source, 'lxml')

text = ""
for paragraph in soup.find_all('p'): #p tag  of wikipedia as it uses paragraphs
    text += paragraph.text
    
#Preprocessing the text
text = re.sub(r"\[[0-9]*\]", " ", text)
text = re.sub(r"\s+", " ", text)
clean_text = text.lower()
clean_text = re.sub(r'\W', ' ', clean_text)
clean_text = re.sub(r'\d', ' ', clean_text)
clean_text = re.sub(r'\s+', ' ', clean_text)

sentences = nltk.sent_tokenize(text)

stop_words = nltk.corpus.stopwords.words('english')

#Histogram
word2count = {}
for word in nltk.word_tokenize(clean_text):
    if word not in stop_words:
        if word not in word2count.keys():
            word2count[word] = 1
        else:
            word2count[word] += 1

#Weighted histogram
for key in word2count.keys():
    word2count[key] = word2count[key]/max(word2count.values())
    
sent2score = {}

for sentence in sentences:
    for word in nltk.word_tokenize(sentence.lower()):
        if word in word2count.keys():
            if len(sentence.split(' ')) < 40:
                if sentence not in sent2score.keys():
                    sent2score[sentence] = word2count[word]
                else:
                    sent2score[sentence] += word2count[word]
                    

best_sentences = heapq.nlargest(5, sent2score, key= sent2score.get)    
print('-------------------------------------------------')
for sentence in best_sentences:
    print(sentence)
