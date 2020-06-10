#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 19:24:21 2020

@author: sahand
"""

class graph():
    """
    A class used to represent a graph

    ...

    Attributes
    ----------
    v : list
        list of vertices
    E : list
        list of edges

    Methods
    -------
    getv()
        returns the vertices list
    """
    def __init__(self,v: list,e: list):
        """ctor for graph

        Args:
            v (list): list of vertices
            e (list): list of edges
        """
        self.v=v
        self.e=e
    def getv(self) -> list:
        """returns the vertices list
        Returns:
            list: a list of vertices
        """
        return self.v
class d_set():
    dst = {}
    def __init__(self,g):
        for v in g.v:
            self.dst[v]=v
    def find(self,ch):
        tmp = ch
        while self.dst[tmp] != tmp: 
            tmp = self.dst[tmp]
        return tmp
    def union(self,a,b):
        cha=self.find(a)
        chb=self.find(b)
        self.dst[chb]=cha
        
def kruskal(g:graph)->list:
    a=[]
    dist_Set = d_set(g)
    egs= sorted(g.e,key=lambda x: x[2])
    for e in egs:
        if dist_Set.find(e[0]) != dist_Set.find(e[1]):
            a.append(e)
            dist_Set.union(e[0],e[1])
    return a
 
v=['a','b','c','d','e','f','g']
e=[('a','b',7),('a','d',5),('b','c',8),('b','d',9),('b','e',7),('c','e',5),
   ('d','e',15),('e','f',8),('f','g',11),('e','g',9),('d','f',6)]
g=graph(v,e)
print(g.getv())
a= kruskal(g)
