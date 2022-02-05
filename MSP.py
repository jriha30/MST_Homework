import csv
import timeit

class Graph:
    def __init__(self):
        pass

    def Read(self, v):
        self.data = list(csv.reader(open(v)))
        self.size = len(self.data)

    def Process(self):
        T = [False] * self.size
        L = [] 
        E = []

        for i in range(self.size):
            if i == 0:
                T[i] = True
            else:
                for j in range(self.size):
                    for k in range(j,self.size):
                        if T[j] != T[k]:
                            E.append([j,k,self.data[j][k]])
                TargetEdge = self.FindMinimum(E)
                L.append(TargetEdge)
                T[TargetEdge[0]] = True
                T[TargetEdge[1]] = True
                E = []
        
        # print(L)
        length = 0
        for ele in L:
            length += int(ele[2])
        print("Minimum Spanning Tree Length is: ", length)


    def OptimizedProcess(self):
        T = [False] * self.size
        L = [] 
        E = []

        for i in range(self.size):
            if i == 0:
                T[i] = True
            else:
                for j in range(self.size):
                    for k in range(j,self.size):
                        if T[j] != T[k]:
                            E.append([j,k,self.data[j][k]])
                TargetEdge = self.FindMinimum(E)
                L.append(TargetEdge)
                # T[TargetEdge[0]] = True
                # T[TargetEdge[1]] = True
                E = []
        length = 0
        for ele in L:
            length += int(ele[2])
        print("Minimum Spanning Tree Length is: ", length)

    def FindMinimum(self, E):
        val = E[0]
        for i in range(len(E)):
            if(val[2] > E[i][2]):
                val = E[i]
        return val

def TestLoop():
    g = Graph()
    g.Read("graph.csv")
    g.Process()

def TestLoopOptimized():
    g = Graph()
    g.Read("graph.csv")
    g.OptimizedProcess()

print(timeit.Timer(TestLoop).timeit(number=1))
print(timeit.Timer(TestLoopOptimized).timeit(number=1))