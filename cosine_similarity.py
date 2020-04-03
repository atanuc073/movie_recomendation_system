#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 23:20:03 2020

@author: atanuc73
"""
from sklearn.feature_extraction.text import CountVectorizer

text=['London Paris London','Paris London Paris']
cv=CountVectorizer()
cv_fit=cv.fit_transform(text)
count_matrix=cv_fit.toarray()
#print(count_matrix)
'''vectors=[]
words=[]
for i in range(0,len(text)):
    dict={'London':0,'Paris':0}
    words=text[i].split(' ')
    for i in words:
        dict[i]+=1
    a=[dict['London'],dict['Paris']]
    vectors.append(a)
print(vectors)
'''
from sklearn.metrics.pairwise import cosine_similarity
similarity_scores=cosine_similarity(count_matrix)























    
    
    