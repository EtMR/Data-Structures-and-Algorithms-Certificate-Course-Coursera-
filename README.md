# Data-Structures-and-Algorithms-Certificate-Course-Coursera-
This repo includes the supplementary materials I created when taking the coursera course on data structure and algorithms

This repo will be basically listing the algorithms I practice on:

# 1. Sort algorithms

Result of the script (using random seed) for selection sort, insertion sort, bubble sort, and merge sort. Considering the run-time, python built-in sort function < merge sort < insertion sort < selection sort < bubble sort.

<pre>
----- Check whether the function runs correctly -----  
original array:  [17, 567, 714, 347, 123, 755, 999, 971, 883, 902]  
built-in sort:   [17, 123, 347, 567, 714, 755, 883, 902, 971, 999]  
----- Our sort algorithm -----  
selection sort:  [17, 123, 347, 567, 714, 755, 883, 902, 971, 999]  
insertion sort:  [17, 123, 347, 567, 714, 755, 883, 902, 971, 999]  
bubble sort:     [17, 123, 347, 567, 714, 755, 883, 902, 971, 999]  
merge sort:      [17, 123, 347, 567, 714, 755, 883, 902, 971, 999]  
</pre>
<pre>
----- Testing on list of length_1000 * 10 times (run-time sec.) -----  
python sort:      0.0009663105010986328  
selecton sort:    0.5036540031433105  
insertion sort:   0.2631814479827881  
bubble sort:      2.131913661956787  
merge sort:       0.046868324279785156  
</pre>
