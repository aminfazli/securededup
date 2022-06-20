class Node:
    def __init__ (self):
        self.l = None
        self.r = None

class Tree:
    def __init__(self):
        self.root = Node()

    def getRoot(self):
        return self.root

    def add(self, bs ):   #bs should be a string with 0,1 characters
        k = 0
        current = self.root
        while k < len(bs):
            if bs[k] == '0':
                if(current.l == None):
                    current.l = Node()
                current = current.l
            else:
                if(current.r == None):
                    current.r = Node()
                current = current.r
            k = k + 1

    def exist(self, bs):
        k = 0
        current = self.root
        while k < len(bs):
            if(bs[k] == '0'):
                if(current.l == None):
                    return False
                current = current.l
            if(bs[k] == '1'):
                if(current.r == None):
                    return False
                current = current.r
            k = k + 1
        return True



