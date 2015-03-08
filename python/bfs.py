#!/usr/bin/python

def bfs(location, depth):
	if (depth == 100):
		return trianglelist[location]
	else:
		return max(bfs(location+depth,depth+1),bfs(location+depth+1,depth+1)