# -*- coding: utf-8 -*-
"""
Created: Fri May 15 15:54:35 2020
@author: Etermeteor
Topic:   sort_algorithms

This script implements different sortng algorithms and compare its performance
Four sorting algorithms are studied here:
    (1) selection sort, (2) insertion sort, (3) bubble sort, & (4) merge sort
"""
import random
import time

def selection_sort(lst):
    """
    Description:
        1. Search through the whole list. Move the min element to idx = 0
        2. Search through the list [1:]. Move the min element to idx = 1
        3. Search through the list [i:]. Move the min element to idx = i
        4. ...  loop through the abovementioned procedure until i = end of the list ...
    Breifly:
        Select the min element and put it to the front for each loop
    Complexity:
        O(n^2)
    """
    
    # Copy the array in order not to change the order of the original array
    lst = lst[:]
    
    for i in range(len(lst)):
        min_idx = i
        for idx in range(i, len(lst)):
            if lst[idx] <= lst[min_idx]:
                min_idx = idx
        lst.insert(i, lst.pop(min_idx))

    return lst

def insertion_sort(lst):
    """
    Description:
        1. Consider a virtual separation of the lst [0] (left) & [1:] (right)
        2. Add the next element [1] from the right lst into the correct place of the left lst
        3. Add the next element [j] from right to left
        4. ...  loop through the abovementioned procedure until i = end of the list ...
    Briefly:
        Insert the right element to the sorted left lst during each loop 
    Complexity:
        O(n^2) - Average case
    """

    # Copy the array in order not to change the order of the original array
    lst = lst[:]

    for i in range(1, len(lst)):
        for j in range(0, i+1):
            if lst[i] <= lst[j]:
                break
        lst.insert(j, lst.pop(i))

    return lst

def bubble_sort(lst):
    """
    Description:
        1. Consider adjacent element [i, i+1] from lst, swap the idx if [i] > [i+1]
        2. ... loop through the list until nothing is swap throughout one full loop...
    Briefly:
        Constantly swapping adjacent until the lst is totally sorted
    Complexity:
        O(n^2) - Average case
    """
    # Copy the array in order not to change the order of the original array
    lst = lst[:]
    
    req_sort = True
    
    while req_sort:
        count = 0
        for i in range(len(lst) - 1):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                count += 1
        if count == 0:
            req_sort = False
    
    return lst
    
def merge_sort(lst):
    """
    Description:
        This part please refer to https://en.wikipedia.org/wiki/Merge_sort
    Breifly:
        Separate the list into sublist and merge sort them back 
    Complexity:
        O(n log(n))
    """
    if len(lst) > 1: 
        mid = len(lst)//2 
        left = lst[:mid]  
        right = lst[mid:]
  
        merge_sort(left)
        merge_sort(right)
        
        i = j = k = 0
        
        while (i < len(left)) and (j < len(right)):
            if left[i] < right[j]:
                lst[k] = left[i]
                i += 1
            else:
                lst[k] = right[j]
                j += 1
            k += 1

        while i < len(left): 
            lst[k] = left[i] 
            i+=1
            k+=1
          
        while j < len(right): 
            lst[k] = right[j] 
            j+=1
            k+=1    

    return lst
                        
def python_sort(lst):
    # Copy the array in order not to change the order of the original array
    lst = lst[:]
    lst.sort()
    return lst

if __name__ == '__main__':
    
    # The tests list can contains duplicates
    tests = {
            'length_10': [random.randint(0, 999) for i in range(10)],
            'length_100': [random.randint(0, 999) for i in range(100)],
            'length_1000': [random.randint(0, 999) for i in range(1000)]
            }
    
    def count_time(funct, lst, num):
        start_time = time.time()
        for i in range(num):
            funct(lst)
        end_time = time.time()
        return end_time - start_time

    print('----- Check whether the function runs correctly -----')
    print('original array: ', tests['length_10'])
    print('built-in sort:  ', python_sort(tests['length_10']))
    print('----- Our sort algorithm -----')
    print('selection sort: ', selection_sort(tests['length_10']))
    print('insertion sort: ', insertion_sort(tests['length_10']))
    print('bubble sort:    ', bubble_sort(tests['length_10']))
    print('merge sort:     ', merge_sort(tests['length_10']))
    print('')
    
    for lst in tests:
        print('----- Testing on list of {} * 10 times -----'.format(lst))
        print('python sort:     ', count_time(python_sort, tests[lst], 10))
        print('selecton sort:   ', count_time(selection_sort, tests[lst], 10))
        print('insertion sort:  ', count_time(insertion_sort, tests[lst], 10))
        print('bubble sort:     ', count_time(bubble_sort, tests[lst], 10))
        print('merge sort:      ', count_time(merge_sort, tests[lst], 10))
        print('')
        
"""
<<<<< RESULTS >>>>>

----- Check whether the function runs correctly -----
original array:  [17, 567, 714, 347, 123, 755, 999, 971, 883, 902]
built-in sort:   [17, 123, 347, 567, 714, 755, 883, 902, 971, 999]
----- Our sort algorithm -----
selection sort:  [17, 123, 347, 567, 714, 755, 883, 902, 971, 999]
insertion sort:  [17, 123, 347, 567, 714, 755, 883, 902, 971, 999]
bubble sort:     [17, 123, 347, 567, 714, 755, 883, 902, 971, 999]
merge sort:      [17, 123, 347, 567, 714, 755, 883, 902, 971, 999]

----- Testing on list of length_10 * 10 times -----
python sort:      0.0
selecton sort:    0.0
insertion sort:   0.0
bubble sort:      0.0
merge sort:       0.0

----- Testing on list of length_100 * 10 times -----
python sort:      0.0
selecton sort:    0.01562047004699707
insertion sort:   0.0
bubble sort:      0.026314258575439453
merge sort:       0.0030221939086914062

----- Testing on list of length_1000 * 10 times -----
python sort:      0.0009663105010986328
selecton sort:    0.5036540031433105
insertion sort:   0.2631814479827881
bubble sort:      2.131913661956787
merge sort:       0.046868324279785156

"""