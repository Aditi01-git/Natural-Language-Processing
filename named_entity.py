# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 01:53:15 2021

@author: Aditi.Dhamat
"""

import nltk

paragraph = "The Taj Mahal was built by Emperor Shah Jahan"

words = nltk.word_tokenize(paragraph)

tagged_words = nltk.pos_tag(words)

namedEnt = nltk.ne_chunk(tagged_words)
namedEnt.draw()

