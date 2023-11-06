#!/usr/bin/env python3
'''
Heapify the array by swapping the smaller children with the root nodes.
First start heapifying from the subtrees and then go up to the root node of
the main tree.'''
def max_heapify(arr, heapsize, i):
    left = 2*i+1
    right = 2*i+2
    largest = i
    
    if(left<heapsize and arr[left]>arr[largest]):
        largest = left
    if(right<heapsize and arr[right]>arr[largest]):
        largest = right
    if(largest != i):
        arr[i],arr[largest] = arr[largest],arr[i]
        max_heapify(arr,heapsize,largest)
    
'''
Build the heap by calling the max_heapify function repeatedly.This function
calls the max_heapify function till the heapsize limit is reached.
'''
def build_heap(arr):
    heapsize = len(arr)
    for i in range((heapsize//2),-1,-1):
        max_heapify(arr,heapsize,i)

'''
Do the actual heapsorting by comparing leaf nodes with the root nodes and
swapping the leaf nodes with the root nodes. Recursively after each heapsorting
step call the max_heapify function. This has to be done to ensure that the
disturbed order of the array is again maintained by heapifying.
'''
def heapsort(arr):
    heapsize = len(arr)
    build_heap(arr)
    print(arr)
    for i in range(heapsize-1,0,-1):
        arr[0],arr[i] = arr[i],arr[0]
        heapsize -= 1
        print(arr[:heapsize],'|',arr[heapsize:])
        max_heapify(arr,heapsize,0)
            
'''
Now, call the main function. Make an array with elements in random order. Call
the heapsort function which iteratively sorts and heapifies the array. After
sorting is complete, print the sorted array.
'''
if __name__ == "__main__":
    arr = [5,2,8,6,3,1,4,9]
    heapsort(arr)
    print(arr)
