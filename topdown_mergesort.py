#! /usr/bin/env python3
# Top-down mergesort implementation

def merge(larr, rarr):
    # Merge two sorted arrays    
    assert larr and rarr, f'merge: array argument length cannot be zero'
    
    print(f'{larr} >> merge << {rarr}', end='')
    
    resarr = []    
    while (larr and rarr):  # both arrays no-empty
        resarr.append(larr.pop(0) if larr[0] <= rarr[0] else rarr.pop(0))
        # ascending sort, exit loop when one array empties

    assert bool(larr) ^ bool(rarr), f'merge: of larr and rarr only one has to be 0 length'
        
    resarr.extend(larr if larr else rarr)
    
    print(f' ---> {resarr}')
    return resarr

    
def mergesort(arr):

    if len(arr) <= 1:   # base case
        return arr
    mid = len(arr)//2
    print(f'{arr} ---> {arr[:mid]} << s p l i t >> {arr[mid:]}')
    return merge(mergesort(arr[:mid]),mergesort(arr[mid:]))

    
if __name__ == "__main__":
    ary = [10,9,8,7,6,5,4,3,2,1]
    print(mergesort(ary))
