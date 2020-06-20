# -*- coding: utf-8 -*-
"""
Created: Fri May 29 10:24:00 2020
@author: Etermeteor
Topic:   minimum cut algorithm

"""
import random
import copy

def random_choose(lst):
    """
    Input 
        list of list with element in the type of string
    Output
        tuple of 2 element
    
    Considering the following case:
        1 2 3 4         1 | 2 3 4
        2 1 4           2 | 1 4
        3 1 4       =>  3 | 1 4
        4 1 2 3         4 | 1 2 3
        choose from one of the right column, for example the "1" in row 2
        then, return 1, 2 as the edge
        for the next function, only the row ids we are interested in need to be considered
    Graph:
        1 - 2
        | \ |
        3 - 4
        
    """
    
    set_lst = []
    
    for element in lst:
        for idx in range(1, len(element)):
            set_lst.append((element[0], element[idx]))

    return random.choice(set_lst)

def min_cut(lst):
    """
    Input is a list of list with each element represent by a string of number
    
    Algorithm:
        
        while len(data) > 2:

            random choose vertices from all [:, 1:] (using the row idx i, j)
            
            for 2 vertices (2 rows of the list):
                combine the [0] element i & j => [i, j]
                merge the [1:] element together

            remove the i, j element in the merged list
            for other rows, replace i, j with i&j
            
        return len(data[0] - 1)
    
    Breifly:
    
    Complexity:
    
    """
    
    while len(lst) > 2:
        # ----- lookup the row idx of the two element -----
        idx = []
        row_element = random_choose(lst)
        if int(row_element[0]) > int(row_element[1]):
            row_element = (row_element[1], row_element[0])
        
        for i in range(len(lst)):
            if lst[i][0] in row_element:
                idx.append(i)
        i, j = idx
        
        # ----- merge i, j -----
        merge = lst.pop(j)      
        lst[i] += merge[1:]
        while row_element[0] in lst[i]: lst[i].remove(row_element[0])
        while row_element[1] in lst[i]: lst[i].remove(row_element[1])
        lst[i].insert(0, row_element[0])
        
        # ----- replace other rows -----
        for k in range(len(lst)):
            if row_element[0] != lst[k][0]:
                while row_element[1] in lst[k]:
                    lst[k].remove(row_element[1])
                    lst[k].append(row_element[0])
    
    return len(lst[0]) - 1
                
if __name__ == '__main__':
    
    with open('kargerMinCut.txt', 'r') as d:
        data = d.readlines()
        
    data = [element.replace('\n', '').split('\t')[:-1] for element in data]        
    print('Number of input list: ', len(data))

    max_iter = 200
    min_count = 100
    
    for i in range(max_iter):
        input_data = copy.deepcopy(data)
        result = min_cut(input_data)
        if result < min_count:
            min_count = result
    print('min cut found after {} times of iteration = {}'.format(max_iter, min_count))
