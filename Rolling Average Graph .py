
# coding: utf-8

# In[62]:

import matplotlib.pyplot as plt 
import numpy as np
import streamer

S = streamer.Streamer('YHOO','YHOO.txt')
price = []
time = []


for i in S.stream():
    price.append(i[2])

avg = []
for i in range(0, len(price)):
    avg.append(sum(price[0:i+1])/(i+1))
    
xs = price
ys = avg

plt.xlabel('Prices')
plt.ylabel('Rolling Avergae')
plt.title('RA vs P')
plt.plot( xs, ys )
plt.show()

