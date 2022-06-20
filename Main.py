from Utils import *
from CSPStore import *
import sys
import itertools


def readInputFile(inputfile):
    with open(inputfile) as f:
        i = 0
        for line in f:
            i = i + 1
            temp = line.split()
            if(len(temp) > 5):
                hashvalues.append(temp[0])
                if(temp[5].isdigit()):
                    views.append(temp[5])
                else:
                    views.append(temp[7])

def convertHashvaluesToBitStrings():
    for i in range(0,n-1):
        hashvalues[i] = stringToBitString(hashvalues[i])

def fillTree(T):
    i = 0
    for w in hashvalues:
        i = i + 1
        print(i)
        T.add(w)

def initialize():
    for i in range(0,N):
        T.add(hashvalues[i])

def agentCommit(i):
    S = []
    count = 0
    h = hashvalues[i]
    for sigma in ["".join(x) for x in itertools.product("01", repeat=logN)]:
        count = count + 1
        if T.exist(sigma):
            S.append(sigma)
        else:
            if isPrefix(sigma, h):
                T.add(h)
                return count
    while len(S) < N:
        sigma = randomChoose(S,k)
        count = count + 1
        if(T.exist(sigma + '0')):
            count = count + 1
            if(T.exist(sigma + '1')):
                S.remove(sigma)
                S.append(sigma + '0')
                S.append(sigma + '1')
            else:
                if isPrefix(sigma+'1', h):
                    T.add(h)
                    return count
                S.remove(sigma)
                S.append(sigma + '0')
        else:
            if isPrefix(sigma+'0',h):
                T.add(h)
                return count
            S.remove(sigma)
            S.append(sigma + '1')
    for sigma in S:
        while len(sigma) < k :
            if isPrefix(sigma,h):
                b = h[len(sigma)+1]
                count = count + 1
                if T.exist(sigma +b):
                    sigma = sigma + b
                else:
                    T.add(sigma + b)
                    return count
            else:
                count = count + 1
                if T.exist(sigma + '0'):
                    sigma = sigma + '0'
                else:
                    sigma = sigma + '1'
    return count

def runSimulation():
    for i in range(0,10000000):
        with open('D:\seaf\Seafile\My Library\outforN15andFile4.txt','a') as f:
            print (i)
            inx = random.randint(0,n-1)
            print (inx)
            f.write(str(inx)+ ' ')
            f.write(str(agentCommit(inx)) + ' ')


hashvalues = []
views = []
readInputFile('4.txt')
N = 15
logN = 4
k = 77
n = len(hashvalues)
convertHashvaluesToBitStrings()
T = Tree()
initialize()
runSimulation()

