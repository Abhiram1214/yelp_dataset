# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 04:26:10 2019

@author: abhiram_ch_v_n_s
"""


import pandas as pd
import json
import matplotlib.pyplot as plt
import seaborn as sns

business = pd.read_json("business.json", lines=True)
checkin = pd.read_json("checkin.json", lines=True)
tip = pd.read_json("tip.json", lines=True)
user = pd.read_json("user.json", lines=True, chunksize=10000)
reviews = pd.read_json("review.json", lines=True, chunksize=10000)


business.columns
'''
Index(['address', 'attributes', 'business_id', 'categories', 'city', 'hours',
       'is_open', 'latitude', 'longitude', 'name', 'postal_code',
       'review_count', 'stars', 'state'],
      dtype='object')
'''

review = pd.DataFrame(columns=['business_id', 'cool', 'date', 'funny', 'review_id', 'stars', 'text', 'useful', 'user_id'])




for review in reviews:
    review = review.append(review)


# for business id OPiPeoJiv92rENwbq76orA

review.loc[review['business_id']=='SbGo2hhUmm_61rRSOPsZGQ']

mask = review['business_id']=='SbGo2hhUmm_61rRSOPsZGQ'

review[['stars', 'text']][mask]

users_less_than_3_rating = review.loc[review['stars'] <= 3]


categories = business['categories']


business['categories'] = business['categories'].str.split(pat = ', ?')



category_count = categories.apply(pd.Series).stack().value_counts().head(20)
category_count

category_count.plot(kind='bar')


business = business.loc[~pd.isna(business['categories'])]

def rest_cat(x):
    return 'Restaurants' in x

restaurants = business.loc[business['categories'].apply(rest_cat)]




restaurants_count = restaurants['categories'].value_counts().head(20)


restaurants_count.plot(kind='bar')





















business.head()
business['categories'] = business['categories'].str.split(pat = ', ?')

category_counts = business['categories'].apply(pd.Series).stack().reset_index(drop=True).value_counts().head(20)


def print_categories(data):
    
     categories_dict = {}
     for i in range(0,20):    
        val = data[i]
        print(val)
        if val in categories_dict:
            categories_dict[val] = 1
        else:
            categories_dict[val] = 1
            
     return categories_dict
    
 
        
business = business.loc[~pd.isna(business['categories'])]


business = business.drop

def process(data):
    mask = []
    for i in range(len(data)):
        if 'Restaurants' in data[i]:
            mask.append(True)
        else:
            mask.append(False)
    return mask

business_updated = process(business['categories'])
business['categories'][business_updated]



def lambdafunc(x):
    return "Restaurants" in x

z = business.loc[business['categories'].apply(lambdafunc),:]

business = business.loc[~pd.isna(business['categories'])]
italian_pizza = business.loc[business['categories'].apply(lambda x: ('Pizza' in x) | ('Italian' in x))]
italian_pizza.to_csv('business_data.csv', columns=['business_id', 'review_count', 'stars', 'state'], index=False)



def find(data):
    categories_dict = {}
    
    for i in range(500):
        print(data[i])
        for j in range(len(data[i])):    
            if data[i][j] in categories_dict:
                categories_dict[data[i][j]] = 1
            else:
                categories_dict[data[i][j]] =+ 1
            
    return categories_dict
            
   
new = find(business['categories'])        
    
    

def print_categories(data):
    
    print(len(data))
 
        
new = business['categories'].apply(print_categories)











  

business['categories'].head()