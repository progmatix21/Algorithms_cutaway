#!/usr/bin/env python3

from time import sleep
import math

'''
A function to help animate bubble sort.  Composes a pre-formatted string
highlighting the two array elements to be swapped (or not). Printing
the embellished string in place, 'animates' it.
'''
class style:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
   
def decorate_array(arr, idx1, idx2, plain_mark=(style.CYAN,style.END), 
                        emph_mark=(style.YELLOW,style.END),emph=False):
	'''
	Returns a decorated string from array arr. The decoration goes
	around the elements with indices idx1 and idx2. The plain deco
	is used when deco is False and the emph deco is used when
	deco is True. deco is True when elements have to swapped in the sort.	
	'''
	deco_str = ''
	for idx,elem in enumerate(arr):
		if idx in [idx1,idx2]:
			mark = [plain_mark,emph_mark][emph] # assigns plain or emph mark based on emph flag
		else:
			mark = ('','')
		
		deco_elem = f'{mark[0]}'+f'{elem:^4}'+f'{mark[1]}' # control deco position
		deco_str += f'{deco_elem:^6}' # print centered
			
	return deco_str


#Bubble sort algorithm with cutaway implentation

def comb_sort(arr,animation=False):
    '''Bubble sort an array with optional animation.'''
    
    #simulate the C ternary operator -- c condition, t true value, f false value
    ternary = lambda c,t,f: [f,t][c]

    gap = len(arr)  #Gap starts as length of array
    k = 1.1  # so called shrink factor
    sorted = False
    
    cmp = 0 # number of comparisons
    swp = 0 # number of swaps
    
    while(not sorted):
        #Gap is floor(gap/k) if this is > 1, else 1
        #Update gap at the beginning of each iteration
        gap = ternary(math.floor(gap/k)>1,math.floor(gap/k),1)
        
        _idx = len(arr)-gap
        for i in range(_idx):
            sorted = True  # set to false if there is a swap in the next scan
            for j in range(_idx-i):
                swap = False
                cmp += 1  
                if(arr[j] > arr[j+gap]): #is a swap needed?
                    swap = True
                if(animation): # if animation is True, print deco based on swap flag
                    print(' '*120,'\r',decorate_array(arr,j,j+gap,emph=[False,True][swap]),'gap:',gap,'cmp:',cmp,'swp:',swp,end='\r')
                    sleep(0.7)
                if(swap):
                    swp += 1
                    arr[j],arr[j+gap] = arr[j+gap],arr[j]
                    sorted = False
            # scan finished with or without swaps
            if(sorted): # no swap happened but was the gap 1?
                if (gap != 1): 
                    sorted = False # we are not done yet
                break
    
    return arr
    
# Basic bubble sort for comparison

def basic_bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            if(arr[j] > arr[j+1]): #is a swap needed?
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

if __name__ == "__main__":
             
    arr = [95,96]+list(range(11))+[97,98]
    arr = list(range(11,0,-1))
    # suggestion: numbers 0 and 99 to avoid the format messing up.
    
    print(*arr)

    print('\n',*comb_sort(arr,animation=True))
    #print('\n',*basic_bubble_sort(arr))

