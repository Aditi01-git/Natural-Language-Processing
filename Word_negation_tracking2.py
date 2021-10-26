# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 03:13:04 2021

@author: Aditi.Dhamat
"""

import nltk
sentence = "I was not happy with the team's performance"

from nltk.corpus import wordnet


#Combining not and happy for negation tracking 
# I am not_happy OR
# I am unhappy

words = nltk.word_tokenize(sentence)

new_words = []

temp_word = ""
for word in words:
    antonyms = []
    if word == "not":
        temp_word = "not_"
    elif temp_word == "not_":
        for syn in wordnet.synsets(word):
            for s in syn.lemmas():
                for a in s.antonyms():
                    antonyms.append(a.name())
        if len(antonyms) >= 1:
            word = antonyms[0]
        else:
            word = temp_word + word
        temp_word = ""
    if word != "not":
        new_words.append(word)
sentence = ' '.join(new_words)