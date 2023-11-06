#!/usr/bin/env python3
import matplotlib.pyplot as plt
import time
from tqdm import tqdm

'''
Three flavours of Fibonacci:
1. top down no memo (classic)
2. top down with memo
3. bottom up with memo (classic dynamic programming)
We time all these 3 for comparison
'''

# The three implementations of Fibonacci

def fib_tdnm(n, cutaway = False):  # Top down, no memory    
    if cutaway: print(n,end='/')
    if n <= 2:
        return 1

    return fib_tdnm(n-1)+fib_tdnm(n-2)

# ======================================================================

def fib_buwm(n):   # Bottom up, with memory
    # Initialise array of n+1
    memo = [-1]*(n+2)      # Minimum array size is 3
    memo[1] = memo[2] = 1  # Initialize first two Fib numbers.
    
    for i in range(1,n+1):
        if memo[i] == -1:   # Not calculated yet
            memo[i] = memo[i-1] + memo[i-2]
        
    return memo[n]

# ======================================================================

def fib_tdwm(n, memo = None, cutaway = False):  # Top down, with memory
    # We pass memo as a persistent array
    if memo == None:  # This is our first call
        memo = [-1]*(n+2)
        memo[1] = memo[2] = 1
        
    if memo[n] == -1:    # Value not yet stored
        memo[n] = fib_tdwm(n-1, memo)+fib_tdwm(n-2, memo)
        if cutaway: print(n,end='/') 
    else:
        if cutaway: print(f"{n}m", end='/') 
        
        
    return memo[n]

# ======================================================================

# Timer decorator
def timer_func(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        res = func(*args, **kwargs)
        end = time.perf_counter()
        return {"result":res, "time":end-start}

    return wrapper

# decorated functions for timing

@timer_func
def timed_fib_tdnm(n):
    return fib_tdnm(n)

@timer_func
def timed_fib_buwm(n):
    return fib_buwm(n)

@timer_func
def timed_fib_tdwm(n):
    return fib_tdwm(n)

    
if __name__ == "__main__":

    i = 15

    res_dict = timed_fib_tdnm(i)
    print(f"\nfib_tdnm({i}) is {res_dict['result']}, taking {res_dict['time']:.4E}s")    

    res_dict = timed_fib_tdwm(i)
    print(f"\nfib_tdwm({i}) is {res_dict['result']}, taking {res_dict['time']:.4E}s")            
    
    res_dict = timed_fib_buwm(i)
    print(f"\nfib_buwm({i}) is {res_dict['result']}, taking {res_dict['time']:.4E}s")            
        
    # Plots showing growth of time for these three methods
    print("Plotting runtimes...")
    
    max_num = 30

    # Allocate memory in advance
    tdnm_times = [0]*(max_num+5)
    tdwm_times = [0]*(max_num+5)
    buwm_times = [0]*(max_num+5)
    
    for n in tqdm(range(1,max_num)):
        tdnm_times[n] = timed_fib_tdnm(n)['time']
        tdwm_times[n] = timed_fib_tdwm(n)['time']
        buwm_times[n] = timed_fib_buwm(n)['time']
        
    plt.plot(tdnm_times[1:max_num],label = "tdnm",lw=6,alpha=0.4)
    plt.plot(tdwm_times[1:max_num],':',label = "tdwm",lw=3,alpha=0.7)
    plt.plot(buwm_times[1:max_num],label = "buwm",lw=6,alpha=0.4)
    plt.xlabel("n")
    plt.ylabel("run time")
    plt.title("Fibonacci run times")
    plt.grid(visible=True)
    plt.legend(loc='best')
    plt.show()
        

