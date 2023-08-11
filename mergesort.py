#!/usr/bin/env python3

import operator

class Mergesort:
    # Implements the top down merge sort algorithm.
    
    def __init__(self, ascending=True, cutaway=False):
        self._ascending = ascending
        self._cutaway = cutaway
                    
    def _rsplit(self, arr):
        # Recursively splits an array and returns subarrays of size 1
        if self._cutaway:
            print('<< s p l i t >>',arr)
        _arr = arr.copy()
        if len(_arr) <= 1:   # edge condition
            return [_arr]

        mid = len(_arr)//2 # the 'middle' dividing point
        
        # now array as two parts -- one slice is [:mid] and another [mid:]
        return [*self._rsplit(_arr[:mid]), *self._rsplit(_arr[mid:])]
            
    def _merge(self,frag1,frag2):
        # Implements a sorted merge with another fragment.        
        # Returns a merge of two sorted arrays
        _sarr1 = frag1.copy()
        _sarr2 = frag2.copy()
        
        # If 1 fragment is empty, return the other fragment
        if not _sarr1:
            return _sarr2
        
        if not _sarr2:
            return _sarr1
        
        # Choose comparison operator based on ascending flag.
        comp_opr = [operator.ge,operator.le][self._ascending]
        pre = _sarr1.pop(0) if comp_opr(_sarr1[0],_sarr2[0]) else _sarr2.pop(0)        
        
        return [pre] + self._merge(_sarr1,_sarr2)        
        
    def get_sorted(self, ary):
        # input unsorted array, returns mergesorted array.
        if len(ary) <= 1:
            return ary
        
        # Split operation: Create a list of arrays with one element each.
        frag_list = self._rsplit(ary)
        # Alternatively, [[e] for e in ary]

        # Merge operation
        while(len(frag_list)>1):
            # Remove element pairs from frag_list,merge them and append to frag_list.
            if self._cutaway:
                print(">>merge<<", frag_list)
            frag_list.append(self._merge(frag_list.pop(0), frag_list.pop(0)))                               
        
        return frag_list[0]   # The only element here is the final merged/sorted list
    
    def __repr__(self):
        # Printable representation of object.
        return f'{self.__class__.__name__}:ascending={self._ascending},cutaway={self._cutaway}'
  

if __name__ == "__main__":

    arr3 = list(range(10,0,-1))
    
    sorter = Mergesort(cutaway=True,ascending=True)
    print(sorter)
    print(sorter.get_sorted(arr3))
    # End
