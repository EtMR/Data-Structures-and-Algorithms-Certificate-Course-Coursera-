# -*- coding: utf-8 -*-
"""
Created: Fri Jun 01 18:17:00 2020
@author: Etermeteor
Topic:   strongest connected component

"""

import numpy as np
from collections import deque 

def process_data(data):
    """
    Input data in the form of (start, end , \n)
    Return the G, and Grev with form of  lst = [[], [4, 5], [8], [6, 4, 7],... ]
    A description of G, and Grev can be found in DFS_loop point (3) 
    
    """
    G = [[] for i in range(875715)]
    Grev = [[] for i in range(875715)]
    
    for line in data:
        i, j = int(line.split(' ')[0]), int(line.split(' ')[1])
        
        if i != j:
            G[i].append(j)
            Grev[j].append(i)
    
    return G, Grev

def DFS_loop(lst):
    """
    (1) order = [0 ~ 875714] defined outside the function
    the order list is modified in the fns and output a list of the finishing time for each vertex
    For example, if the vertices are finished in a order of 3, 5, 2, 8,...
    The order list will be [0, 3, 5, 2, 8,...], with the first element is 0
    
    (2) leadr = [0] * 875715 defined outside the function
    Here, I keep track of the exploration of vertices by checking their leader value.
    If leader value == 0, the vertex is not explored yet.
    By so, we don't need an extra list to store to exploring information.
    
    (3) The input is constructed by a list of lists.
    Each element list contains the ends of a arc and the index is its starts.
    For example, lst = [[], [4, 5], [8], [6, 4, 7],... ]
    The element in lst[3] indicates there are three arcs (3, 6), (3, 4), & (3, 7)
    The first element is always an empty list.
    
    """
    
    global t; t = 0
    global s
    
    sys_order = order[:]
    
    for i in range(L, 0, -1):
        i_map = sys_order[i]

        if leader[i_map] == 0:
            s = i_map
            DFS(lst, i_map)

def DFS(lst, i):
    global t
    global s
    
    leader[i] = s
    stack = deque([i])
    
    while len(stack) > 0:
        ele = stack[-1]        
        is_complete = True

        for j in lst[ele]:

            
            if leader[j] == 0:
                leader[j] = s
                stack.append(j)
                is_complete = False
            
        if is_complete == True:
            t += 1
            od = stack.pop()
            order[t] = od

if __name__ == '__main__':
    """
    # Some facts about this assigment
    # Vertices are labeled as positive integers from 1 to 875714
    # There are total 5,105,043 edges, including self-loop.
    # Each vertices are represented by i row in the data file with the form (start, end , \n)
    """
    
    # ----- 1. Let Grev = (G with all arcs reversed) -----
    # test_option main is the main assignment dataset. 
    # test_option 1 is a sanity check by using the test dataset provided in the lecture
    test_option = 'main'

    print('----- Process Grev -----')
    if test_option == 'main':
        with open('SCC.txt', 'r') as d:
            data = d.readlines()
        G, Grev = process_data(data)
        L = len(G) -1

    if test_option == '1':
        G = [[], [4], [8], [6], [7], [2], [9], [1], [6, 5], [3, 7]]
        Grev = [[], [7], [5], [9], [1], [8], [8, 3], [4, 9], [2], [6]]
        L = len(G) - 1
    print('')

    # ----- 2. Run DFS_Loop on Grev -----
    # Calculate order from Grev
    print('----- DFS Grev -----')
    order = list(np.arange(L+1))
    leader = [0] * (L+1)
    DFS_loop(Grev)
    print('Successfully calculate the magical order from Grev')
    print('')

    # ----- 3. Run DFS_Loop on G -----
    # Calculate leader from G
    print('----- DFS G -----')
    leader = [0] * (L+1)
    DFS_loop(G)
    print('Successfully calculate the leaders for all vertices')
    print('')
    
    # ----- 4. Count leader element using dictionary -----
    # Using the leader list to count (number of) the max 5 SCC groups
    count_dict = {}
    for i in leader:
        if i in count_dict.keys():
            count_dict[i] += 1
        else:
            count_dict[i] = 1
            
    val = list(count_dict.values())
    val.sort(reverse=True)
    print('# of top 5 SCC groups = ', val[:5])
    # of top 5 SCC groups =  [434821, 968, 459, 313, 211]
    # Total runtime is < 30 s when running on my personal laptop