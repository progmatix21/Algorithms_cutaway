#!/usr/bin/env python3

#Binary search using iterative method

from time import sleep

def binarysearch(arr,elem,animation=False):
    '''Binary search using iterative method.
       Input:array and element to search
       Output:index of element found, else None'''
       
    low = 0
    high = len(arr)-1
    mid = (low+high)//2
    
    _arr = sorted(arr)   # sort the array
    
    for e in _arr:
        print(f'{e: >5}', end='')
    print()
    
    while (high >= low):
        if (animation):
            bar = ['' for i in range(len(_arr))] #init empty bar
            bar[low] += 'L' # place H,M,L markers at proper positions
            bar[mid] += 'M'
            bar[high] += 'H'
            for e in bar:
                print(f'{e: >5}',end='')
            print(f'    {low},{mid},{high}')
            sleep(1)
        if elem == _arr[mid]:
            return mid
                       
        if elem < _arr[mid]:
            high = mid-1            
        else:  
            low = mid+1

        mid = (low+high)//2
        
    return None         #Nothing found

if __name__ == "__main__":
    #arr = [2,3,4,5,6,7,18,21,1,9,45,100]
    arr = [2,3,4,5,6,7,18,21,1,9,45,100]
    elem = 1


    print(f'Found {elem} at pos: {binarysearch(arr,elem,animation=True)}')
    
    
    
