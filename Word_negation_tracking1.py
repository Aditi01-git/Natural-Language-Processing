# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 03:02:43 2021

@author: Aditi.Dhamat
"""
import nltk
sentence = "I was not happy with the team's performance"

#Combining not and happy for negation tracking 
# I am not_happy OR
# I am unhappy

words = nltk.word_tokenize(sentence)

new_words = []

temp_word = ""
for word in words:
    if word == "not":
        temp_word = "not_"
    elif temp_word == "not_":
        word = temp_word + word  #not_happy
        temp_word = ""
    if word != "not":
        new_words.append(word)
sentence = ' '.join(new_words)


