# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 12:20:38 2019

@author: Anu Nema
"""
def get_title_from_index(index):
    return df[df.index == index]["title"].values[0]
def get_index_from_title(title):
    return df[df.title == title]["index"].values[0]
#define a sample text
text=["London Paris London","Paris Paris London"]
#cv is the object count vectorizer of class
cv=CountVectorizer()
#a variable to store the vector of text
count_matrix=cv.fit_transform(text)
#toarray convert matrix into array
print((count_matrix).toarray())
#calculation of cosine similarity
similarity_scores=cosine_similarity(count_matrix)
print(similarity_scores)
#read dataset from the excel file
#df is a variable name
df=pd.read_csv("movies_imdb.csv")
#to print columns from database
print(df.columns)
#select some features
combine_features=['keywords','cast','genres','director']
#fill blank with space
for feature in features:
    df[feature]= df[feature].fillna('')
#create a column in dataframe in to combine features
#definning a funtion
def combine_features(row):
    #attachment in row
    return row['keywords'] +" "+ row['cast'] +" "+ row ['genres'] +" "+row['director']   
    
df["combine_features"]=df.apply(combine_features,axis=1)
#to print top 5 strings
print(df["combine_features"].head())     
#converting the features into vectors

cv=CountVectorizer()

count_matrix=cv.fit_transform(df["combine_features"])
#using cosine fromula we are checking the similarity 
cosine_sim=cosine_similarity(count_matrix)     
#printing the cosine similarity          
print((count_matrix).toarray())

movie_user_likes="Avatar"
#to get the index of movie
movie_index=get_index_from_title(movie_user_likes)
print(movie_index)

#list of tuple of similarity movies
similar_movies=list(enumerate(cosine_sim[movie_index]))


#sort the tuple
sorted_similar_movies = sorted(similar_movies,key= lambda x:x[1],reverse=True)

print(sorted_similar_movies)
#to print the title
i=0
for movie in sorted_similar_movies:
    print(get_title_from_index(movie[0]))
    i=i+1
    if i>5:
        break


















