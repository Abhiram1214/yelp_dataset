<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 04:26:10 2019

@author: abhiram_ch_v_n_s
"""


import pandas as pd
import json
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
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

pizza_reviews.to_csv('pizza_reviews', columns=['business_id', 'cool', 'date', 'funny', 'review_id', 'stars', 'text', 'useful', 'user_id'])



#-----------review and business csv's

businesses = pd.read_csv('business_list.csv')
business_ids = businesses['business_id'].values
pizza_reviews = pd.read_csv('pizza_reviews.csv')

good_reviews = pizza_reviews.loc[pizza_reviews['stars'] == 5, 'text'].str.lower()
bad_reviews = pizza_reviews.loc[pizza_reviews['stars'] <= 3, 'text'].str.lower()



good_corpus = good_reviews[:1000]
bad_corpus = bad_reviews[:1000]


good_corpus = ' '.join(review for review in good_corpus)
bad_corpus = ' '.join(review for review in bad_corpus)

stopwords = set(STOPWORDS)
stopwords.update(["pizza", "good", 'great', "well", "restaurant"])



#wordcloud

wordcloud = WordCloud(stopwords=stopwords,max_font_size=50, max_words=100, background_color="white").generate(bad_corpus)

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')




#users with most reviews
    
most_reviews = elite_users.sort_values(by='review_count', ascending=False).head()
    

#total reviews from the most freq cusotmer
most_visited_user = most_reviews.iloc[0]
most_visited_user_review = pizza_reviews.loc[pizza_reviews['user_id'] == most_visited_user['user_id']]


#bad reviews that a restaruant received from the max_user

most_visited_user_review['stars'] #only 1 review from the user


#oldest usr on yelp

oldest_user = elite_users.sort_values(by='yelping_since', ascending=False).head(1)


#users with elite status
elite_users = user_df.loc[user_df['elite'] != '']

#most freq user's most freq business
user_business_id = pizza_reviews.loc[pizza_reviews['user_id'] == most_visited_user['user_id']]
freq_business_id = user_business_id['business_id']
    

#most freq user's less visited business
les_freq_business = user_business_id['business_id']



#highest rated businessess
































<<<<<<< HEAD
'''
=======
'''
=======
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

pizza_reviews.to_csv('pizza_reviews', columns=['business_id', 'cool', 'date', 'funny', 'review_id', 'stars', 'text', 'useful', 'user_id'])



#-----------review and business csv's

businesses = pd.read_csv('business_list.csv')
business_ids = businesses['business_id'].values
pizza_reviews = pd.read_csv('pizza_reviews.csv')

good_reviews = pizza_reviews.loc[pizza_reviews['stars'] == 5, 'text'].str.lower()
bad_reviews = pizza_reviews.loc[pizza_reviews['stars'] <= 4, 'text'].str.lower()



good_corpus = good_reviews[:1000]
bad_corpus = bad_reviews[:1000]


good_corpus = ' '.join(review for review in good_corpus)
bad_corpus = ' '.join(review for review in bad_corpus)

#wordcloud

wordcloud = WordCloud(max_font_size=50, max_words=100,background_color="white").generate(good_corpus)

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')

wordcloud.to_file('good_review.png')








>>>>>>> 06f25eb744258d2a37cd7876c20f82ce719a04bf
>>>>>>> 0d7125248e0d7196cf0e7580472b9b2a1ba89440
