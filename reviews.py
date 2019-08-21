# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 23:12:27 2019

@author: abhiram_ch_v_n_s
"""

import pandas as pd
import json 
import matplotlib.pyplot as plt

review_reader = pd.read_json('review.json', lines=True, chunksize=100000)

type(review_reader)


for r in review_reader:
    review_ids = r['business_id']


#business_id 
business_ids = business['business_id'].values
 

mask = []


for i in review_ids:
    for j in business_ids:
        if i == j:
            mask.append(True)
        else:
            mask.append(False)





    