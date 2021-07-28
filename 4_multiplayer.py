
import numpy as np
from collections import deque

#we want to create the vertex to hold values like neighbours, depth etc.
class vertex:
    def __init__(self, i, j, char, former):
        #self.position = (i, j) #up/down, left/right respectively
        self.depth = None # to be updated
        self.neighbours = []
        self.char = char
        self.former = former



class initialize:

    def __init__(self, N, maze, stop): # indicated it needs maze as input
        self.stop = stop
        self.maze = maze
        self.N = N
        self.vertices = {}

    def check(self, pos):
        #checking position and character
        i, j = pos
        if pos not in self.vertices: # if never seen

            if i > -1 and i < self.N and j > -1 and j < self.N: #position check
                if self.maze[i][j] not in self.stop: # character check
                    return True

        return False




    def find_neighbours(self, i, j):
        # removing spaces in directions
        possible_neighbours = [ (i, j-1),
                                (i, j+1),
                                (i-1, j),
                                (i+1, j) ]

        neighbours = []
        for pos in possible_neighbours:
            #i, j = pos # getting coordinates
            if self.check(pos): # legal pos and not wall
                neighbours.append(pos) # fulfilled and added

        return neighbours # return the neighbours



    # in this class so that we keep the self
    def BFS(self, pacman_pos):
        queue = deque() # initializing LIFO for BFS

        for pac in pacman_pos:
            y, x = pac
            self.vertices[y, x] = vertex(y, x, maze[y][x], former = pacman_pos)
            self.vertices[y, x].depth = 0
            queue.append(pac)

        while len(queue) > 0:
            (y, x) = queue.popleft()
            parent = self.vertices[y, x]
            parent.neighbours = self.find_neighbours(y, x)
            for pos in parent.neighbours:

                i, j = pos
                nb = vertex(i, j, maze[i][j], former = (y, x))
                nb.depth = parent.depth + 1
                self.vertices[i, j] = nb

                if nb.char == 'G':
                    return (nb.depth)

                queue.append(pos)
        return ('', False)




if __name__ == '__main__':

    #size
    N = int(input())

    #if N == 1: # just to make sure :)
    #    print('No ghost is reachable.')

    maze = [0]*N # initialize
    pacman_pos = [] # list

    for i in range(N):
        maze[i] = list(input()) # constructing row-wise
        #Append all pacmen to list:
        for j in range(N):
            if maze[i][j] == 'P':
                pacman_pos.append((i, j))
    
    stop = ['#', 'P'] # also use pacman
    minimum = np.inf
    G = initialize(N, maze, stop) # just saving the self. variables
    closest = G.BFS(pacman_pos)

    print(closest)