

import numpy as np
from collections import deque

#we want to create the vertex to hold vales like neighbours, depth etc.
class vertex:
    def __init__(self, i, j, char):
        self.position = (i, j) #up/down, left/right respectively
        self.depth = None # to be updated
        self.neighbours = []
        self.char = char

class build:

    def __init__(self, maze, stop): # indicated it needs maze as input
        self.vertices = self.create_graph(maze)
        self.find_neighbours(stop) # finding possible neighbours and updating vertices


    def create_graph(self, maze):
        #we want to create a dict which holds the class of a vertex based on position
        vertices = {}

        for i in range(N):
            for j in range(N):
                vertices[ (i,j) ] = vertex(i, j, maze[i][j]) #object created
        return vertices

    def find_neighbours(self, stop):

        for (i, j) in self.vertices.keys():
            # i is up/down, j is left/right# to get the x and y
            possible_neighbours = [ (self.vertices.get( (i, j-1) ), 'W '),
                                    (self.vertices.get( (i, j+1) ), 'E '),
                                    (self.vertices.get( (i-1, j) ), 'N '),
                                    (self.vertices.get( (i+1, j) ), 'S ')
                                    ]

            for (neighbour, dir) in possible_neighbours:
                if neighbour is not None and neighbour.char != stop:
                    self.vertices[(i, j)].neighbours.append((neighbour, dir))


    # in this class so that we keep the self
    def BFS(self, pacman_pos):
        # s holds all the values of the vertex

        s = self.vertices[ pacman_pos ] # start from top left
        s.depth = '' # has to be 1 for codejudge
        queue = deque() # just to initialize
        # we make opposite of enqueue and dequeue as append and pop left
        queue.append(s)
        ghost_found = False

        while len(queue) > 0:
            v = queue.popleft() # think of v as s, just in the loop
            #this makes the list updated
            for (neighbour, dir) in v.neighbours:

                if neighbour.depth == None: # none if not visited

                    if neighbour.char == 'G': # first/closest ghost found
                        ghost_found = True
                        path = v.depth + dir # the optimal path
                        return path


                    neighbour.depth = v.depth + dir # this also makes it marked

                    queue.append(neighbour) # makes us loop thought the front every time

        if not ghost_found:
            path = str()

        return path



if __name__ == "__main__":
    #size
    N = int(input())
    maze = [0]*N # initialize
    for i in range(N):
        maze[i] = list(input())
    # If maze is 1x1
    if N == 1:
        path = str()

    else:
        found = False
        for i in range(N):
            for j in range(N):
                if maze[i][j] == 'P':
                    pacman_pos = (i, j)
                    found = True
                    break

        stop = '#'
        G = build(maze, stop)
        if found:
            path = G.BFS(pacman_pos)
        else:
            path = str()

    print(path)

