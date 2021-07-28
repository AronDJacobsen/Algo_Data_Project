

'''

8
########
P #    #
# # ## #
# #  #G#
#    ###
#### # #
#G   #G#
########

'''
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
        self.vertices, self.pacman_pos = self.create_graph(maze)
        self.find_neighbours(stop) # finding possible neighbours and updating vertices

    def create_graph(self, maze):
        #we want to create a dict which holds the class of a vertex based on position
        vertices = {}

        for i in range(N):
            for j in range(N):
                vertices[ (i,j) ] = vertex(i, j, maze[i][j]) #object created
                if maze[i][j] == 'P':
                    pacman_pos = (i, j)
        return vertices, pacman_pos

    def find_neighbours(self, stop):

        for (i, j) in self.vertices.keys():
            # i is up/down, j is left/right# to get the x and y
            possible_neighbours = [ self.vertices.get( (i, j-1) ),
                                    self.vertices.get( (i, j+1) ),
                                    self.vertices.get( (i-1, j) ),
                                    self.vertices.get( (i+1, j) )
                                    ]

            for neighbour in possible_neighbours:
                if neighbour is not None and neighbour.char != stop:
                    self.vertices[(i, j)].neighbours.append(neighbour)


    # in this class so that we keep the self
    def DFS(self, pacman_pos):
        # s holds all the values of the vertex

        s = self.vertices[ pacman_pos ] # start from top left
        s.depth = 1 # has to be 1 for codejudge
        queue = deque() # just to initialize
        # we make opposite of enqueue and dequeue as append and pop left
        queue.append(s)
        nghosts = 0
        while len(queue) > 0:
            # pops the right most element
            v = queue.pop() # think of v as s, just in the loop
            #this makes the list updated
            for neighbour in v.neighbours:

                if neighbour.depth == None: # none if not visited

                    if neighbour.char == 'G':
                        nghosts += 1

                    neighbour.depth = v.depth + 1 # this also makes it marked

                    queue.append(neighbour) # makes us loop thought the front every time
        return nghosts

if __name__ == "__main__":
    #size
    N = int(input())
    maze = [0]*N # initialize
    for i in range(N):
        maze[i] = list(input())

    stop = '#'
    G = build(maze, stop)
    nghosts = G.DFS(G.pacman_pos)
    print(nghosts)

