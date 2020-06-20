# Data-Structures-and-Algorithms-Certificate-Course-Coursera-
This repo includes the supplementary materials I created when taking the coursera course on data structure and algorithms

This repo will be basically listing the algorithms I practice on:

# CLASS I
# 1. sort_algorithms

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

# 2. integer_multiplication  
This script implements the Karatsuba Multiplication for assignment #1. Instead of only testing on the problem stated in the question. I randomly tested the self-implemented function on three other cases (1) 4 digits * 4 digits, (2) 16 digits * 16 digits, and (3) 64 digits * 64 digits and compared the run-time with built-in "*" multiplcation function. The results are demonstrated below:

<pre>
----- 4 digits * 4 digits -----
int1 =  8220
int2 =  2914
Built-in function result: 23953080. 
Time spent = 0.0
Self-imp function result: 23953080. 
Time spent = 0.0
</pre>
<pre>
----- 16 digits * 16 digits -----
int1 =  1816443250374164
int2 =  9489599478642800
Built-in function result: 17237318921734899720426904619200. 
Time spent = 0.0
Self-imp function result: 17237318921734899720426904619200. 
Time spent = 0.0009970664978027344
</pre>
<pre>
----- 64 digits * 64 digits -----
int1 =  2104968846162103373550783363667652680876105070442868653658730193
int2 =  9106622569741617123023598256414743024930855512733701923471688264
Built-in function result: 19169156803062780553833643737303685851029158853411054207058261243539486089719694174798845780526550791659499570766564832180554952. 
Time spent = 0.0
Self-imp function result: 19169156803062780553833643737303685851029158853411054207058261243539486089719694174798845780526550791659499570766564832180554952. 
Time spent = 0.008986949920654297
</pre>
<pre>
----- Programming Assignment #1 -----
int1 =  3141592653589793238462643383279502884197169399375105820974944592
int2 =  2718281828459045235360287471352662497757247093699959574966967627
Built-in function result: 8539734222673567065463550869546574495034888535765114961879601127067743044893204848617875072216249073013374895871952806582723184. 
Time spent = 0.0
Self-imp function result: 8539734222673567065463550869546574495034888535765114961879601127067743044893204848617875072216249073013374895871952806582723184. 
Time spent = 0.0056438446044921875
</pre>

# 3. count_inv  
This script implements the count inversion function for assignment #2. I also randomly tested the self-implemented function on an array with 10 integer (0~10) with random order for sanity check. According to the lecture, the count_inv function is piggybacking on the merge sort method; thus, sorted a sorted function is returned when calling the count_inv function. The results are demonstrated below:

<pre>
----- Sanity Check -----
san_chk arr:  [0, 4, 1, 6, 3, 2, 9, 5, 7, 8] (Input array)
function output (arr, count):  ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10)  
(Standard output from my function: sorted array, count of inversion)

----- Assignment #2 -----
Input array: IntegerArray.txt
Count of inversions: 2407905288, time used: 2.1146366596221924.
</pre>

# 4. quicksort  
This script implements the quicksort function for assignment #3. Combined with the sorting algorithm, the number of comparison during the partition phase is also counted and returned. Three different methods for choosing the pivot is implemented (first element, last element, & median element).

<pre>
----- Sanity Check -----
san_chk arr:  [0, 4, 1, 6, 3, 2, 9, 5, 7, 8]
function output (arr, count):  ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 26)

----- Assignment #3 -----
(Method 1) # of comparison using pivot = arr[0]:  162085
(Method 2) # of comparison using pivot = arr[-1]:  164123
(Method 3) # of comparison using pivot = median:  138382
</pre>

# CLASS II
# 1. Strongly Connected Component
The script implements the calculation of strongly connected component for assignment #1. It is worth mentioning that the recurrisive method for depth-first search (DFS) was implemented before. However, it runs pretty slow and kills the kernel easily. Therefore, an alternative iterative method was implemented in this work. A test dataset using the graph (shown below) in the lecture note is also provided in the scipt for sanity check.

<img src="./images/CLASS2 Assignment1.png" width="300" height="250">
A schematic of the process flow using the test dataset.  

<pre>
----- Assignment #1 -----
# of top 3 SCC groups =  434821, 968, and 459
</pre>

