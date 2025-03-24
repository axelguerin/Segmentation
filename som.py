from random import random
from math import sqrt

def d_manhattan(a, b):
    sum = 0
    for i in range(len(a)):
        sum += abs(a[i] - b[i])
    return sum

def d_euclidienne(a, b):
    sum = 0
    for i in range(len(a)):
        sum += (a[i] - b[i]) ** 2
    return sqrt(sum)

def d_neuronne(xA, yA, xB, yB):
    return abs(xA - xB) + abs(yA - yB)

class SOM():

    def __init__(self, X, epsilon_0, T_max, map_size):
        self.X = X
        self.n = len(X[0])
        self.epsilon_0 = epsilon_0
        self.T_max = T_max
        self.map_size = map_size
        self.W = self.init_W()
        self.X = self.init_X()
        
    def init_W(self):
        W = []
        for i in range(self.map_size):
            W.append([])
            for j in range(self.map_size):
                W[i].append([])
                for k in range(self.n):
                    W[i][j].append(random())
        return W

    def init_X(self):
        with open("iris.csv", "r") as f:
            content = f.read()
        X = content.split("\n")
        for i in range(len(X)):
            X[i] = X[i].split(",")
        X.pop(0)
        for i in range(len(X)):
            X[i].pop(4)
        for i in range(len(X)):
            for j in range(len(X[i])):
                X[i][j] = float(X[i][j])
        return X



som = SOM([[1,1,1,1]], 0.01, 100, 10)


