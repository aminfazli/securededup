import random

def charToBitString(x):
    return str(bin(ord(x)))[2:];

def stringToBitString(x):
    out = ''
    for c in x:
        out = out + charToBitString(c);
    return out

def isPrefix(x,y):
    if(y.startswith(x)):
        return True
    else:
        return False

def randomChoose(L,k):
    while True:
        tt = random.choice(L)
        if len(tt) < k:
            return tt
