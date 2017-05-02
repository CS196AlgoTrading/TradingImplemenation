import matplotlib.pyplot as plt 
import numpy as np
import streamer

S = streamer.Streamer('YHOO','YHOO.txt')
price = []
time = []


for i in S.stream():
    price.append(i[2])
    time = range(len(price))
avg = []
for i in range(len(price)):
    avg.append(sum(price[:i+1])/(i+1))
    
xs = time 
ys = avg

plt.xlabel('Time')
plt.ylabel('Rolling Avergae')
plt.title('RA vs Time')
plt.plot( xs, ys )
plt.show()

