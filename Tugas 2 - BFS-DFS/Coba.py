# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 11:29:11 2021

@author: Alvian
"""

graph = {
  '1' : set(['2','3']),
  '2' : set(['1', '4','5']),
  '3' : set(['1','6']),
  '4' : set(['2']),
  '5' : set(['2']),
  '6' : set(['3']),
}
#BFS
visited = [] # List to keep track of visited nodes.
queue = []     #Initialize a queue

def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)

  while queue:
    s = queue.pop(0) 
    print (s, end = " ") 

    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

# Driver Code
print('BFS nya seperti dibwah ini :')
bfs(visited, graph, '1')
print('')
print('')
#DFS
visited = set() # Set to keep track of visited nodes.

def dfs(visited, graph, node):
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# Driver Code
print('DFS nya seperti dibawah ini :')
dfs(visited, graph, '1')