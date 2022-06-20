import matplotlib.pyplot as plt

def averageNumberOfQueriesPerFileStore(inputfile):
    counts = []
    files = []
    with open(inputfile) as f:
        i = 0
        for line in f:
            for x in line.split():
                if i % 2 == 0:
                    files.append(int(x))
                else:
                    counts.append(int(x))
                i = i + 1
    i = 0.0
    S = 0
    avg = [0.0]
    for x in counts:
        S = S * (i / (i+1)) + x / (i+1)
        avg.append(S)
        i = i+1
    for i in range(len(avg),size):
        avg.append(S)
    return avg


size = 1000
avg2= averageNumberOfQueriesPerFileStore('C:\\Users\\Amin Fazli\\Works\\Seafile\\My Library\\outforN2andFile4.txt')
avg2= avg2[0:size]
print(len(avg2))
avg4= averageNumberOfQueriesPerFileStore('C:\\Users\\Amin Fazli\\Works\\Seafile\\My Library\\outforN4andFile4.txt')
avg4= avg4[0:size]
print(len(avg4))
avg8= averageNumberOfQueriesPerFileStore('C:\\Users\\Amin Fazli\\Works\\Seafile\\My Library\\outforN8andFile4.txt')
avg8= avg8[0:size]
print(len(avg8))
avg16= averageNumberOfQueriesPerFileStore('C:\\Users\\Amin Fazli\\Works\\Seafile\\My Library\\outforN16andFile4.txt')
avg16= avg16[0:size]
print(len(avg16))

x = []
for i in range (0,size):
    x.append(i)
p2 = plt.plot(x,avg2)
p4 = plt.plot(x,avg4)
p8 = plt.plot(x,avg8)
p16 = plt.plot(x,avg16)
plt.legend((p2[0],p4[0],p8[0],p16[0]), ('N=2', 'N=4', 'N=8', 'N=16'),loc="")
plt.ylabel('Average Number of Queries (Q)')
plt.xlabel('Number of Users (n)')
plt.show()