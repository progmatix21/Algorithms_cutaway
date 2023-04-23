#!/usr/bin/env python3

'''
This is implementation of a 0/1 knapsack class with two methods: classical bottom-
up dynamic programming and top-down with memo.
'''

import numpy as np

class Knapsack():
    '''Class to implement knapsack
       Instantiate with (capacity,weights,values)
       Returns solution matrix, best value, weights picked
    '''
    def __init__(self, capacity = 0, weights = [], values = []):
        # Initialize capacity weights and values, add a leading 0 for ease of
        # computation.
        self._capacity = capacity
        self._weights = [0]+weights
        self._values = [0]+values
        # Initialize solution matrix
        self._V = np.zeros((len(self._weights),self._capacity+1), dtype=int)
        self._V[1:,1:] = -1 # except first row and col, all values -1
        # They get filled via the algorithm
        
    def _pack_bottom_up(self, ):  # deemed private function
        # We traverse the V matrix column-wise for a classical bottom-up dynamic
        # programming approach.

        for j in range(1,self._capacity+1):
            for i in range(1,len(self._weights)):
                # Implement the two recurrence equations here
                if(j-self._weights[i] >= 0):
                    self._V[i,j] = max(self._V[i-1,j], self._values[i]+self._V[i-1,j-self._weights[i]])
                else:
                    self._V[i,j] = self._V[i-1,j]
                  
        return None
        
    def _pack_top_down(self, i , j):    # deemed private function
        # i is index of weight/value j is knapsack capacity
        # go top-down but with memory. Top-down computes only needed sub-problems.
        # memory avoids recomputations.  Best of both worlds.
        if self._V[i,j] < 0:
            if j < self._weights[i]:
                self._V[i,j] = self._pack_top_down(i-1,j)
            else:
                self._V[i,j] = max(self._pack_top_down(i-1,j), self._values[i]+self._pack_top_down(i-1,j-self._weights[i]))                

        return self._V[i,j]
        
    def _get_best_weights(self, ):
        # Get the most valuable weights picked.
        r = len(self._weights)-1
        c = self._capacity
        included_list = []   # Included weight indices

        while(True):
            while self._V[r, c] == self._V[r-1, c]:
                r = r-1
                if r == 0:
                    break
                    
            if r > 0:            
                included_list.append(r)            
                c = c - self._weights[r]
                r = r - 1

            if r == 0 or c <= 0:
                break
                
        return included_list[::-1] # return indices in ascending order.
        
    def pack(self, how = 'bottom_up'):
        # Public interface to pack the knapsack. Default is bottom-up
        # Initialise the solution space for each call
        self._V = np.zeros((len(self._weights),self._capacity+1), dtype=int)
        self._V[1:,1:] = -1 # except first row and col, all values -1
        # They get filled via the algorithm        
        
        # Calling these functions, fills the solution matrix (_V)
        if how == 'bottom_up':
            self._pack_bottom_up()
        else:
            self._pack_top_down(len(self._weights)-1, self._capacity)
            
        # We return the state of the knapsack or the solution
        return self._V, self._V[-1,-1], self._get_best_weights()
        # (solution matrix, best value, weights selected)

                    
if __name__ == "__main__":

    # Instantiate a knapsack
    #my_knapsack = Knapsack(capacity = 5, weights = [2,1,3,2], values = [12,10,20,15])

    my_knapsack = Knapsack(capacity = 10, weights = [2,1,3,2,5,7,8], values = [12,10,20,15,17,28,24])
    print("Capacity:", my_knapsack._capacity, "\nWeights:", my_knapsack._weights[1:], "Values:", my_knapsack._values[1:])
        
    solution_matrix, best_value, best_weights = my_knapsack.pack(how = 'top_down')
    print("Top down solution matrix:\n", solution_matrix)
    print("Best value:", best_value)    
    print("Best weights:", best_weights)    # Print the weight indices, 1 based indexing
    
    solution_matrix, best_value, best_weights = my_knapsack.pack(how = 'bottom_up')
    print("Bottom up solution matrix:\n", solution_matrix)
    print("Best value:", best_value)    
    print("Best weights:", best_weights)

