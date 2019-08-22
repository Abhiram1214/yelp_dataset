# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 04:26:10 2019

@author: abhiram_ch_v_n_s
"""


import pandas as pd
import json
import matplotlib.pyplot as plt
import seaborn as sns
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

business = pd.read_json("business.json", lines=True)
checkin = pd.read_json("checkin.json", lines=True)
tip = pd.read_json("tip.json", lines=True)
user = pd.read_json("user.json", lines=True, chunksize=10000)
review_reader = pd.read_json("review.json", lines=True, chunksize=10000)


business.columns
'''
Index(['address', 'attributes', 'business_id', 'categories', 'city', 'hours',
       'is_open', 'latitude', 'longitude', 'name', 'postal_code',
       'review_count', 'stars', 'state'],
      dtype='object')
'''


review_df = pd.DataFrame(columns=['business_id', 'cool', 'date', 'funny', 'review_id', 'stars', 'text', 'useful', 'user_id'])


for review in review_reader:
    review_df = review_df.append(review)

# for business id OPiPeoJiv92rENwbq76orA

review.loc[review['business_id']=='SbGo2hhUmm_61rRSOPsZGQ']

mask = review['business_id']=='SbGo2hhUmm_61rRSOPsZGQ'

review[['stars', 'text']][mask]

users_less_than_3_rating = review.loc[review['stars'] <= 3]


business['categories'] = business['categories'].str.split(pat = ', ?')

categories = business['categories']





category_count = categories.apply(pd.Series).stack().value_counts().head(20)
category_count

category_count.plot(kind='bar')


business = business.loc[~pd.isna(business['categories'])]

def rest_cat(x):
    return 'Restaurants' in x

restaurants = business.loc[business['categories'].apply(rest_cat)]



restaurants_count = restaurants['categories'].value_counts().head(20)


restaurants_count.plot(kind='bar')


def pizzas(x):
    return ('Pizza' in x) | ('Italian' in x)

pizza_rest = business.loc[business['categories'].apply(pizzas)]

pizza_rest.to_csv('business_list.csv', columns=['business_id', 'review_count', 'stars', 'state'], index=False)

#tip:   ['business_id', 'compliment_count', 'date', 'text', 'user_id'], dtype='object')

'''
#business: (['address', 'attributes', 'business_id', 'categories', 'city', 'hours',
       'is_open', 'latitude', 'longitude', 'name', 'postal_code',
       'review_count', 'stars', 'state'],
      dtype='object')
    
review: 

['business_id', 'cool', 'date', 'funny', 'review_id', 'stars', 'text',
       'useful', 'user_id'],
      dtype='object'    
'''

businesses = pd.read_csv('business_list.csv')
business_ids = businesses['business_id'].values

#reviews_updated = [review.loc[review['business_id'].apply(lambda x: x in business_ids)] for review in review_reader]

def pizzas_review(x):
    return x in business_ids

pizza_reviews = review_df.loc[review_df['business_id'].apply(pizzas_review)]




good_reviews = pizza_reviews.loc[pizza_reviews['stars'] == 5]
bad_reviews = pizza_reviews.loc[pizza_reviews['stars'] <= 4]

a_user = good_reviews.iloc[1]['user_id']

pizza_reviews.loc[pizza_reviews['user_id'] == 'tU-4DhNg8JjCHwzzNe3ojQ']








import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, r'C:\Users\abhiram_ch_v_n_s\Desktop\yelp_casestudy\yelp_dataset\wordcloud')



from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
























