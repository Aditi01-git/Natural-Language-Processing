# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 17:00:51 2021

@author: Aditi.Dhamat
"""

from gensim.models import KeyedVectors

filename = 'GoogleNews-vectors-negative300.bin'

model = KeyedVectors.load_word2vec_format(filename, binary= True)

model.wv.most_similar('king')

#Adding /Subtracting words as vectors

model.wv.most_similar(positive=['king', 'woman'], negative=['man'])