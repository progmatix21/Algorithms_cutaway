#! /usr/bin/env python3

import random

def longest_subsequence(s1, s2, s3):
    '''Input: three sequences.  Repeat one sequence if you have only two.
       Output: tuple with length of LCS, matching subsequence indices in
               sequence 1,2 and 3 respectively.
    '''

    ls1 = [None] + list(s1).copy()   # padding to help with edge conditions
    ls2 = [None] + list(s2).copy()
    ls3 = [None] + list(s3).copy()
        
    m, n, r = len(ls1), len(ls2), len(ls3)

    #---------------------------------
    memo = [(0,0,0,0)] # sparse--will have info only on non-zero matches.    
    # Searches for and returns the longest substring in the space preceding a triple intersection.
    max3d = lambda i,j,k: max([tup for tup in memo if (
                          tup[1] < i  and tup[2] < j and tup[3] < k)],
                          default=(0,0,0,0))   

    for i in range(1,m):
        for j in range(1,n):
            for k in range(1,r):
                if (ls1[i] == ls2[j]) and (ls2[j] == ls3[k]):  # match at i,j,k
                    memo.append((max3d(i,j,k)[0]+1, i, j, k))
    #---------------------------------
    res = []   # Structure to return result
    p,q,v = m,n,r
    
    last_term = max(memo) # tuple with longest subseq length and coordinates
    res.append(last_term) # append to result data

    p,q,v = last_term[1], last_term[2], last_term[3]

    while (maxtup := max3d(p,q,v))[0] > 0:
        res.append(maxtup)
        p,q,v = maxtup[1],maxtup[2],maxtup[3]
        
    if len(res) == 1:  # No common sequence found
        return (0,[],[],[])
        
    res = res[::-1]   # Reverse to get ascending order
    # array of subseq indices in s1,s2,s3
    _, is1, is2, is3 = list(zip(*res)) 
    
    # Convert these to 0 based indices
    is1 = [e-1 for e in is1]
    is2 = [e-1 for e in is2]
    is3 = [e-1 for e in is3]
        
    return(len(is1), is1, is2, is3)
                        
if __name__ == "__main__":
    # Generate three random alphanumeric sequences
    # numerals, upper and lower case    
    chars = [chr(c+48) for c in range(10)] + \
            [chr(c+65) for c in range(26)] + \
            [chr(c+97) for c in range(26)]

    rnd_str = lambda length: [random.choice(chars) for _ in range(length)]
    s1,s2,s3 = rnd_str(70), rnd_str(75), rnd_str(80)

    # Test case for non-overlapping strings
    # s1,s2,s3 = "abcdefg","hijklmn","opqrstu"
    
    print("The three strings:")
    print(''.join(s1),''.join(s2),''.join(s3), sep='\n' )
    
    print("\nLength of longest subsequence, its indices in s1,s2,s3")
    print(result := longest_subsequence(s1,s2,s3))
    # To get the literal subsequence, filter (say) s1 using its lcs indices
    print("Longest subsequence in s1,s2,s3: ",[s1[i] for i in result[1]])

