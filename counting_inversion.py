# -*- coding: utf-8 -*-
"""
Created: Fri May 19 13:36:00 2020
@author: Etermeteor
Topic:   counting_inversion

This script implements the counting inversion algorithm. 
(week 2 - divide and conquer - algorithm 1)
"""

import random
import time

def count_inv(arr):
    """        
    Pesudocode:
        
        count(arr):

            length arr = n

            if n = 1:
                return 0

            else:
                x_sorted, x_count = on left arr
                y_sorted, y_count = on right arr
                arr_sorted, count = intermixed arr
                return (1)+(2)+(3)

        Note:   If we can implement the count intermixed arr with O(n),
                the function will be able to run at time O(n log (n))
        
    Complexity:
        O(n log (n))
    """
    
    l = len(arr)
    
    if l == 1:
        return arr, 0
    
    else:
        half_l = l // 2
        x_sorted, x = count_inv(arr[:half_l])
        y_sorted, y = count_inv(arr[half_l:])
        
        # implement O(n) for arr_sorted, z = CountSplitInv(arr, n)
        i = j = k = z = 0
        
        while (i < len(x_sorted)) and (j < len(y_sorted)):
            if x_sorted[i] < y_sorted[j]:
                arr[k] = x_sorted[i]
                i += 1
            else:
                arr[k] = y_sorted[j]
                j += 1
                z += len(x_sorted) - i
            k += 1

        while (i < len(x_sorted)):
            arr[k] = x_sorted[i]
            i += 1
            k += 1

        while (j < len(y_sorted)):
            arr[k] = y_sorted[j]
            j += 1
            k += 1

    return arr, x+y+z

if __name__ == '__main__':

    random.seed(123)
    
    def evl(funct, x):
        start_time = time.time()
        _, result = funct(x)
        end_time = time.time()
        return result, (end_time - start_time)

    with open('IntegerArray.txt', 'r') as IA:
        testset = IA.readlines()
        
    san_chk = random.sample(range(0, 10), 10)
    testset = [int(element) for element in testset]

    print('----- Sanity Check -----')
    print('san_chk arr: ', san_chk)
    print('function output (arr, count): ', count_inv(san_chk))
    print('')
    print('----- Assignment #2 -----')
    print('Count of inversions: {}, time used: {}.'.format(*evl(count_inv, testset)))
    
"""

----- Sanity Check -----
san_chk arr:  [0, 4, 1, 6, 3, 2, 9, 5, 7, 8]
function output (arr, count):  ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10)

----- Assignment #2 -----
Count of inversions: 2407905288, time used: 2.1146366596221924.

"""