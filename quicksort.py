# -*- coding: utf-8 -*-
"""
Created: Fri May 25 10:41:00 2020
@author: Etermeteor
Topic:   quicksort

This script implements the programming assignment #3

Note: my system has a maximum recursive limit = 3000
    import sys
    sys.getrecursionlimit()
"""

import math
import time
import random

def quicksort(method, arr, l, r, count):
    """
    Pivot chosen method 
        1: choose the first element
        2: choose the last element
        3: choose the median element (value) in the set of {first, middle, last}
    
    arr input array
    
    l is the left most index in arr we are interested in
    r is the right most (index+1) in arr we are interested in
    
    count is the # of comparison that the algorithm runs through during sorting
    
    """
    
    if r - l == 0:
        return arr, count
    
    else:
        if method == 1:
            pass
            
        elif method == 2:
            arr[l], arr[r - 1] = arr[r - 1], arr[l]
            
        elif method == 3:
            med = l + math.ceil((r-l)/2) - 1
            choose = [(arr[l], l), (arr[med], med), (arr[r-1], r-1)]
            choose.sort()
            idx = choose[1][1]
            arr[l], arr[idx] = arr[idx], arr[l]
            
        else:
            return '--- Not a defined method for this assignment ---'
        
        # ----- Choose pivot accordingly -----        
        pivot = arr[l]
        i = l + 1
        
        # ----- Implement the partition method -----
        for j in range(l + 1, r):
            if arr[j] < pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                
        arr[l], arr[i - 1] = arr[i - 1], arr[l]

        count += r - l - 1

        arr, count = quicksort(method, arr, l, i-1, count)
        arr, count = quicksort(method, arr, i, r, count)

        return arr, count

if __name__ == '__main__':

    random.seed(123)
    
    def evl(funct, x):
        start_time = time.time()
        _, result = funct(x)
        end_time = time.time()
        return result, (end_time - start_time)

    with open('QuickSort.txt', 'r') as QS:
        testset = QS.readlines()
    
    san_chk = random.sample(range(0, 10), 10)
    testset = [int(element) for element in testset]

    print('----- Sanity Check -----')
    print('san_chk arr: ', san_chk)
    print('function output (arr, count): ', 
          quicksort(1, san_chk, 0, len(san_chk), 0))
    print('')
    print('----- Assignment #3 -----')
    print('(Method 1) # of comparison using pivot = arr[0]: ', 
          quicksort(1, testset[:], 0, len(testset), 0)[1])
    print('(Method 2) # of comparison using pivot = arr[-1]: ', 
          quicksort(2, testset[:], 0, len(testset), 0)[1])
    print('(Method 3) # of comparison using pivot = median: ', 
          quicksort(3, testset[:], 0, len(testset), 0)[1])

"""
----- Sanity Check -----
san_chk arr:  [0, 4, 1, 6, 3, 2, 9, 5, 7, 8]
function output (arr, count):  ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 26)

----- Assignment #3 -----
(Method 1) # of comparison using pivot = arr[0]:  162085
(Method 2) # of comparison using pivot = arr[-1]:  164123
(Method 3) # of comparison using pivot = median:  138382

"""    