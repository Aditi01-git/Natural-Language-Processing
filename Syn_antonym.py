# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 02:58:46 2021

@author: Aditi.Dhamat
"""

from nltk.corpus import wordnet

synonyms = []
antonyms = []

for syn in wordnet.synsets("good"):
    for s in syn.lemmas():
        synonyms.append(s.name())
        for a in s.antonyms():
            antonyms.append(a.name())
            
            
print(set(synonyms))
print(set(antonyms))