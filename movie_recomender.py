#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 00:15:56 2020

@author: atanuc73
"""

import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
#####helper functions. use them when needed #############
def get_title_from_index(index):
    return df[df.index == index]["title"].values[0]
def get_index_from_title(title):
    return df[df.title ==title]["index"].values[0]
########################################################

#Step1 read CSV
df=pd.read_csv("movie_dataset.csv")
#print (df.columns)

# Step 2  : get the Features

features=['keywords','cast','genres','director']

# fill features which is N/A
for feature in features:
    df[feature]=df[feature].fillna('')

# Step 3 : Create a column in Df Which Combines all selected Features
def combine_features(row):
    try:
        return row['keywords']+' '+row['cast']+' '+row['genres']+' '+row['director']
    except:
        print("Error",row)

df["combine_features"]=df.apply(combine_features,axis=1)
#print(df['combine_features'].head())

#Create count matrix from this new combined column
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
cv=CountVectorizer()
count_matrix=cv.fit_transform(df['combine_features'])

# Compute the cosine similarity based on the count matrix

cosine_sim=cosine_similarity(count_matrix)

movie_user_like=str(input("Enter The Movie Name :"))

#Get index of this movie from its title
movie_index=get_index_from_title(movie_user_like)
similar_movies=list(enumerate(cosine_sim[movie_index]))

## Step 7: Get a list of similar movies in descending order of similarity score
sorted_similar_movies=sorted(similar_movies,key=lambda x:x[1],reverse=True)

## Step 8 : Print titles of first 50 movies

i=0
for movie in sorted_similar_movies:
    print (get_title_from_index(movie[0]))
    i+=1
    if i>25:
        break
    



























