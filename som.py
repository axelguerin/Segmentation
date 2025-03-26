from random import random, randint
from math import sqrt, inf, exp

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

    def __init__(self, epsilon_0, T_max, map_size):
        self.epsilon_0 = epsilon_0
        self.T_max = T_max
        self.map_size = map_size
        self.sigma_0 = 0.5 * map_size
        self.X = self.init_X()
        self.n = len(self.X[0])
        self.W = self.init_W()
        
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
    
    def fit(self):
        for t in range(self.T_max):
            n = randint(0, len(self.X) - 1)

            i_min = 0
            j_min = 0
            d_min = inf

            for i in range(self.map_size):
                for j in range(self.map_size):
                    d = d_manhattan(self.X[n], self.W[i][j])
                    if d < d_min:
                        d_min = d
                        i_min = i
                        j_min = j
            
            sigma = self.sigma_0 * exp(-t / self.T_max)
            epsilon = self.epsilon_0 * exp(-t / self.T_max)

            for i in range(self.map_size):
                for j in range(self.map_size):
                    d = d_neuronne(i_min, j_min, i, j)
                    theta = exp(- (d * d) / (2 * sigma * sigma))
                    for k in range(self.n):
                        self.W[i][j][k] += theta * epsilon * (self.X[n][k] - self.W[i][j][k])

    def assign(self):
        self.assignment = []
        for t in range(len(self.X)):
            i_min = 0
            j_min = 0
            d_min = inf

            for i in range(self.map_size):
                for j in range(self.map_size):
                    d = d_manhattan(self.X[t], self.W[i][j])
                    if d < d_min:
                        d_min = d
                        i_min = i
                        j_min = j
            self.assignment.append([i_min, j_min])
        return self.assignment




som = SOM(0.01, 10000, 2)
som.fit()
assignment = som.assign()

M = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

for t in range(len(assignment)):
    i = 0
    j = 0
    if assignment[t] == [0, 0]:
        i = 0
    if assignment[t] == [0, 1]:
        i = 1
    if assignment[t] == [1, 0]:
        i = 2
    if assignment[t] == [1, 1]:
        i = 3
    if t < 50:
        j = 0
    elif t < 100:
        j = 1
    else:
        j = 2
    M[i][j] += 1

print(M)