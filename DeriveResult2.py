import matplotlib.pyplot as plt
import math


x = range(1,17)
y = [0,153.5, 228.3, 303, 377.7, 450.6, 524.3, 593.8, 672, 745, 817,889, 960, 1030, 1101, 1173.5]
z = []
for i in x:
    z.append(i*(77-math.floor(math.log(i,2))) + math.floor(math.log(i,2)))
p1 = plt.plot(x,y)
p2 = plt.plot(x,z, '--')
plt.xlabel('Degree of Anonymity (N)')
plt.ylabel('Average Number of Queries (Q)')
plt.legend((p1[0],p2[0]),('Average Number of Queries', 'Theoretical Upper Bound'))
plt.show()