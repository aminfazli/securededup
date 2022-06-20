import random
import math
import matplotlib.pyplot as plt


def averageNumberOfQueries():
    global m
    S = 0.0
    avg = []
    for i in range(N,size):
        S = S + pow(2,k) / (m-i)
        x = random.randrange(0,files)
        if (x > m):
            m = m + 1
        avg.append(S)
    print(N)
    return avg

k = 77
N = 2
m = N+1
files = 500000
size = 10000000
avg = averageNumberOfQueries()
p2 = plt.plot(avg)
N = 4
m = N+1
avg = averageNumberOfQueries()
p4 = plt.plot(avg)
N = 8
m = N+1
avg = averageNumberOfQueries()
p8= plt.plot(avg)
N = 16
m = N+1
avg = averageNumberOfQueries()
p16 = plt.plot(avg)
plt.ylabel('Log of Average Number of Queries (log(Q))')
plt.xlabel('Number of Users (n)')
plt.legend((p2[0], p4[0], p8[0],p16[0]), ('N=2', 'N=4', 'N=8', 'N=16'),loc="lower right")
plt.show()


