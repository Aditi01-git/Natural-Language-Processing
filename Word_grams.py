# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 01:32:03 2021

@author: Aditi.Dhamat
"""

import nltk
import random
import numpy as np

#text = """Global warming or climate change has become a worldwide concern.It is a concern and is causing melting glaciers,changing weather patterns, rising sea levels, floods, cyclones and droughts. Global warming implies an increase in the average temperature of the Earth due to entrapment of greenhouse gases in the earth's atmosphere."""
text = """Thank you all so very much. Thank you to the Academy. Thank you to all of you in this room. I have to congratulate the other
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
n = 10

ngrams = {}

words = nltk.word_tokenize(text)

for i in range(len(words) - n):
    gram = ' '.join(words[i:i+n])
    if gram not in ngrams.keys():
        ngrams[gram] = []
    ngrams[gram].append(words[i+n])
    
currentGram = ' '.join(words[0:n])
result = currentGram

for i in range(100):
    if currentGram not in ngrams.keys():
        break
    possibilities = ngrams[currentGram]
    nextItem = possibilities[random.randrange(len(possibilities))]
    result += ' '+nextItem
    rwords = nltk.word_tokenize(result)
    currentGram = ' '.join(rwords[len(rwords)-n:len(rwords)])
    
print(result)