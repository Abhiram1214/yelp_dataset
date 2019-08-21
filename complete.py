# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 01:58:47 2019

@author: abhiram_ch_v_n_s
"""
import pandas as pd
import matplotlib.pyplot as plt


business = pd.read_json('business.json', lines=True)

business.head()
business.columns


drop_cols = ['address', 'attributes', 'hours', 'is_open', 'latitude', 'longitude', 'name', 'postal_code']
business = business.drop(drop_cols, axis=1)

business['categories'] = business['categories'].str.split(pat = ', ?')

category_counts = business['categories'].apply(pd.Series).stack().value_counts().head(20)

category_counts.plot(kind='bar')

pd.isna(business['categories']).sum()

business = business.loc[~pd.isna(business['categories'])]


#restarants in categories
business = business.loc[business['categories'].apply(lambda x: 'Restaurants' in x), :]



italian_pizza = business.loc[business['categories'].apply(lambda x: ('Pizza' in x) | ('Italian' in x))]



italian_pizza.to_csv('business_list.csv', columns=['business_id', 'review_count', 'stars', 'state'], index=False)


#------------------------------------------------------

businesses = pd.read_csv('business_list.csv')

review_reader = pd.read_json('review.json', lines=True, chunksize=100000)

business_ids = businesses['business_id'].values


reviews_updated = [review.loc[review['business_id'].apply(lambda x: x in business_ids)] for review in review_reader]

reviews_updated = pd.concat(reviews_updated)

'''
for review in review_reader:
    review_business = review
    

def func(x):
    return x in business_ids

reviews = review_business.loc[review_business['business_id'].apply(func),:]
'''

reviews_updated.to_csv('reviews_filtered.csv', index=False)


#------------------reviews


reviews_filter = pd.read_csv('reviews_filtered.csv')


review_count = reviews_filter['stars'].value_counts()

reviews_filter.loc[reviews_filter['stars'] == 5]

review_count.plot(kind='bar')


good_reviews = reviews_filter.loc[reviews_filter['stars'] == 5, 'text']
bad_reviews = reviews_filter.loc[reviews_filter['stars'] < 4, 'text']


good_reviews = good_reviews.iloc[:1000].str.lower()
bad_reviews = bad_reviews.iloc[:1000].str.lower()

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator












