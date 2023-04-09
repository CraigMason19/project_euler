#-------------------------------------------------------------------------------
# Name:        Problem 107.py
#
# Notes:
#
# Links:
#
# TODO:         
#-------------------------------------------------------------------------------

from operator import *
from math import *

def GenerateNodeNames(n):
    s = ""
    while(n >= 0): 
        s = chr(int(n%26) + 97) + s;
        n = floor(n / 26) - 1;
    return s;

def Prim(matrix):
    Nodes = [GenerateNodeNames(i) for i in range(len(matrix[0]))]

    # The weight of the graph before (mirrored in the matrix)
    l = []
    for i in range(0, len(Nodes)):
        l.extend(matrix[i][i+1:])
    TotalWeight = sum(x for x in l if x != '-')
 
    # Create a dictionary of lists representing our graph
    Graph = {}
    for i, node in enumerate(Nodes):
        Graph[node] = {Nodes[i] : x for i, x in enumerate(matrix[i]) if x != '-'} 
        Graph[node] = sorted(Graph[node].items(), key=itemgetter(1))

    # Save weight
    NodesFound = [Nodes[0]]
    Weight = 0
    Edges = []

    for i in range(1, len(Nodes)):
        PossibleNodes = []
        for node in NodesFound:
            for k,v in Graph[node]: 
                if k not in NodesFound:
                    PossibleNodes.append([k,v, node])
                    break #continue
        next = min(PossibleNodes, key=lambda x: x[1])
        NodesFound.append(next[0])
        Edges.append(next[2]+'->'+next[0])
        Weight += next[1] 

    print(Edges, Weight)
    print('A saving of %s\n' % (TotalWeight - Weight)) 

Matrix = [['-', 7,   '-', 5,   '-', '-', '-'],
         [7,   '-', 8,   9,   7,   '-', '-'],
         [8,   '-', '-', 5,   '-', '-', '-'],
         [5,   9,   '-', '-', 15,  6,   '-' ],
         ['-', 7,   5,   15,  '-', 8,   9],
         ['-', '-', '-', 6,   8,   '-', 11],
         ['-', '-', '-', '-', 9,   11,  '-']]

Matrix2 = [['-', 16, 12, 21, '-', '-', '-'],
      	  [16, '-', '-', 17, 20, '-', '-'],
          [12, '-', '-', 28, '-', 31, '-'],
 	      [21, 17, 28, '-', 18, 19, 23],
          ['-',	20, '-', 18, '-', '-', 11],
       	  ['-',	'-', 31, 19, '-', '-', 27],
          ['-', '-', '-', 23, 11, 27, '-']]


def Do(x):
    if x != '-':
        return int(x)
    return x

f = open('./Problems 101 - 150/network.txt', "r")
Matrix3 = []
for line in f.readlines():
    line = line.replace('\n', '')
    line = line.split(',')
    Matrix3.append([Do(x) for x in line])

Prim(Matrix)
Prim(Matrix2)    
Prim(Matrix3)