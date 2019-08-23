# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 05:34:09 2019

@author: Abhiram_CH_V_N_S
"""

import numpy as np
import matplotlib.pyplot as plt

fig, _ = plt.subplots()

rng = np.arange(50)
rnd = np.random.randint(0, 10, size=(3, rng.size))


fig, ax = plt.subplots(figsize=(10,5))
yrs = 1950 + rng




ax.stackplot(yrs, rng + rnd, labels=['Eastasia', 'Eurasia', 'Oceania'])
ax.legend(loc='upper left')
#ax.set_xlim(xmin=yrs[0], xmax=yrs[-1])
fig


x = np.random.randint(low=1, high=11, size=50)
y = x + np.random.randint(1, 5, size=x.size)
data = np.column_stack((x, y))


fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(8, 4))
ax1.scatter(x=x, y=y, marker='o', c='r', edgecolor='b')

ax2.hist(data, bins=np.arange(data.min(), data.max()), label=('x', 'y'))
fig




fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(7, 7))
ax1, ax2, ax3, ax4 = ax.flatten()


















