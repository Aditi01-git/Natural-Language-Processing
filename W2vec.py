# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 16:36:10 2021

@author: Aditi.Dhamat
"""

import bs4 as bs
import urllib.request
import re
import nltk
from gensim.models import Word2Vec
from nltk.corpus import stopwords

#Getting the data(Scraping- parsing articles)
source = urllib.request.urlopen("https://en.wikipedia.org/wiki/Climate_change").read()

soup = bs.BeautifulSoup(source, 'lxml')

text = ""
for paragraph in soup.find_all('p'): #p tag  of wikipedia as it uses paragraphs
    text += paragraph.text
    
#Preprocessing the text
text = re.sub(r"\[[0-9]*\]", " ", text)
text = re.sub(r"\s+", " ", text)
text = text.lower()
text = re.sub(r'[@#\$%&\*\(\)\<\>\?\'\":;\]\[-]', ' ', text)
text = re.sub(r'\d', ' ', text)
text = re.sub(r'\s+', ' ', text)

#Preparing the data
sentences = nltk.sent_tokenize(text)

sentences = [nltk.word_tokenize(sentence) for sentence in sentences]

for i in range(len(sentences)):
    sentences[i] = [word for word in sentences[i] if word not in stopwords.words('english')]
#Training Wrod2Vec model
model = Word2Vec(sentences, min_count=1)


words = model.wv.vocab

vector = model.wv['global']

similar = model.wv.most_similar('warming')