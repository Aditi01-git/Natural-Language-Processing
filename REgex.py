# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 01:21:37 2021

@author: Aditi.Dhamat
"""

#Regex

import regex as re

sen = "I was born in 1992"
#Replaces with space at every digit encountered
sen1 = re.sub(r"\d", "", sen)
print(sen1)

#.* is for 0 or more characters
print(re.match(r".*", sen))

sen2 = ""
#.+ is for 1 or more characters
print(re.match(r".+", sen2))

print(re.match(r"[a-zA-Z]+", sen))

sen3 = "abb"
# ? matches 0 or only 1 character mentioned before it
#Like here it matches 0 or 1 'b' after a
print(re.match(r"ab?", sen3))

#Note: Match only looks at first pattern in the sentence
#It does not look further after it finds some pattern.
#For ex:
sen4 = "1992 was the year when I was born"
print(re.match(r"[a-zA-Z]+", sen4))
#Here , even if we have alphabets , it outputs none as 
# it does not look further than 1992(first element only , local search)

# search fn does global search
print(re.search(r"[a-zA-Z]+", sen4))

# ^ caret is used for starts with some character,
# sentence start with some character/pattern

if re.match(r"^1992", sen4):
    print("Match")
else:
    print("No Match")
    
# $ is for identifying last character/ pattern
#can't use match fn here as it checks only first pattern
if re.search(r"born$", sen4):
    print("Match")
else:
    print("No Match")

#Substitution
sen5 = "I love Avengers"

#re.sub fn does global search and replace
print(re.sub(r"Avengers", "Justice League", sen5))


#re.I flag to case of characters
print(re.sub(r"[a-z]", "0", sen5, flags=re.I))

# here 1 specifies the count of characters to be replaced
print(re.sub(r"[a-z]", "0", sen5, 1, flags=re.I))

#Shorthand character classes
sent1 = "welcome to the new year party 2021"

sent2 = "Just ~% +++--- arrived at @Jack's place. #fun"

sent3 = "I       love      you"

print(re.sub(r"\d", "", sent1)) #Digit replace
print(re.sub(r"[@%'~+\.#]","", sent2)) #Match group of chars
print(re.sub(r"\w", " ", sent2)) #Remove word chars
sent2_mod = (re.sub(r"\W", " ", sent2)) #Keep only word chars

print(sent2_mod)

sent2_mod = re.sub(r"\s+", " ", sent2_mod) #Space replacement

#1 or more spaces with '+'
sent2_mod = re.sub(r"\s+[a-zA-Z]\s+", " ", sent2_mod)

sent3_mod = re.sub(r"\s+", " ", sent3)

# '-' means range of chars, for ex: [@#%$+-\.] --> this means it 
# will try to find range of chars from + to .

"""So, in our example, "+-\."  means the range of characters 
from "+"  to "."  in terms of their ASCII value 
(the range from 43-46), not the three characters themselves. 
In our case this mistake doesn't 
result in an error and still works as the range 43-46 
is a valid range. But, by mistake if you put here 
something like "+-#"  then it would result into an error 
as the ASCII range would 43-35 which is invalid.

Therefore, the best thing to do whenever you want 
to just track "-"  is to escape it, i.e. "\-" ."""


#Preprocessing using regex

X = ["This is a wolf #scary",
     "Welcome to the jungle #missing",
     "11322 the number to know",
     "Remember the name s - John",
     "I     love     you"]

for i in range(len(X)):
    X[i] = re.sub(r"\W", " ", X[i])
    X[i] = re.sub(r"\d", " ", X[i])
    X[i] = re.sub(r"\s+[a-z]\s+", " ", X[i], flags=re.I)
    X[i] = re.sub(r"\s+", " ", X[i])
    X[i] = re.sub(r"^\s", "", X[i])
    X[i] = re.sub(r"\s$", "", X[i])





    






