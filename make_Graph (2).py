#!/usr/bin/python
from igraph import *
from csv import reader
import matplotlib.pyplot as plt
import collections
import re

def read_subredditScore(filename):
    f=open(filename, "r")
    dict = {}
    for line in f:
        #row=re.split(r'\s{2,}', line)
        row = line.split()
        if len(row) != 3:
            print(row)
        dict[row[0]] = int(row[-1])
    return dict

def read_edgelist(filename):
    f=open(filename, "r")
    data = []
    self = []
    for line in f:
        edge = line.split()
        if edge[0]==edge[1]:
            self.append(edge)
        data.append(edge)
    return data, self

def Initial(g, subreddit_score, original_submissions):
    for row in original_submissions:
        v = g.vs.find(name = str(row[0]))
        v["karma"] += int(row[3])/int(subreddit_score[row[2]])
    return g

def O(u, subreddit_score):
    e_out = g.incident(u,mode="OUT")
    for edge in e_out:
        if int(subreddit_score[g.es[edge]["subreddit"]]) != 0:
            u["karma"] += int(g.es[edge]["score"])/int(subreddit_score[g.es[edge]["subreddit"]])
        
    
def I(u,subreddit_score):
    n_in = g.neighbors(u,mode="IN")
    for vertex in n_in:
        edge = g.get_eid(vertex,u)
        if int(subreddit_score[g.es[edge]["subreddit"]]) != 0:
            u["karma"] += (int(g.es[edge]["score"])/int(subreddit_score[g.es[edge]["subreddit"]]))*(g.vs[vertex]["karma"]/g.vs[vertex].degree(type="out"))


# read the directed graph, with its edge attributes set
data, original_submissions = read_edgelist("same_image")

# Make the network
g = Graph.TupleList(data, directed=True, vertex_name_attr="name", edge_attrs=["subreddit","score"])

# returns a dictionary array with subreddit scores
subreddit_score = read_subredditScore("subreddit")

# set initial karma of all vertices equal to zero
g.vs["karma"] = 0.0

# Step One: Set karma due to original submissions
g = Initial(g, subreddit_score, original_submissions)

# remove self loops
g.simplify(multiple=False, loops=True)

# for out edges
for vertex in g.vs:
    O(vertex, subreddit_score)

# for in edges
for vertex in g.vs:
    I(vertex, subreddit_score)

for vertex in g.vs:
    print(vertex["name"],vertex["karma"])

# Calculate karma:
#
# I(u) = My original submissions (How about giving initial score based on this?)
# R(u) = In coming edges
# O(u) =  Out going edges
