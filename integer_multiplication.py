# -*- coding: utf-8 -*-
"""
Created: Fri May 18 12:23:00 2020
@author: Etermeteor
Topic:   interger_multiplication

This script implements the programming assignment #1
"""

import random
import time

def int_mul(int1, int2):
    """
    Description:
        output int1 * int2 (both are int)
        length int1 & length int2 & 2 == 0
    Pesudocode:
        (1) int1 = 10^(n/2)a + b, int2 = 10^(n/2)c + d
        (2) int1 * int2 = 10^n*ac + 10^(n/2)(ad + bc) + bd
        (3) recursively calculate ac, ad+bc, bd
        * trick for ad+bc = (a+b)*(c+d) - ac - bd
    Complexity:
        O(?)
    """
    int1 = str(int1)
    int2 = str(int2)

    if len(int1) == 1 and len(int2) == 1:
        return int(int1) * int(int2)
    
    else:
        assert(len(int1) % 2 == 0)
        assert(len(int2) % 2 == 0)
        assert(len(int1) == len(int2))
                
        # --- Separate int1, int2 into a, b, c, d
        m = len(int1)//2 # m = n/2
        a = int1[:m]
        b = int1[m:]
        c = int2[:m]
        d = int2[m:]
                
        ac = int_mul(a, c)
        bd = int_mul(b, d)
        # I do think to avoid the issue when a+b or c+d exceed the current digit.
        # For example, when a = 82, b = 20 -> (a+b) = 102 will break the recursive loop
        ad = int_mul(a, d)
        bc = int_mul(b, c)
            
        result = (10**(2*m))*ac + (10**m)*(ad + bc) + bd

    return result

def python_mul(int1, int2):
    return int1*int2

if __name__ == '__main__':

    random.seed(1234)
    
    def evl(funct, int1, int2):
        start_time = time.time()
        result = funct(int1, int2)
        end_time = time.time()
        return result, (end_time - start_time)
    
    # --- Test on three different cases ---
    # (1) 4 digits * 4 digits
    int1_4 = random.randint(1e3, 1e4)
    int2_4 = random.randint(1e3, 1e4)

    # (2) 16 digits * 16 digits
    int1_16 = random.randint(1e15, 1e16)
    int2_16 = random.randint(1e15, 1e16)
    
    # (3) 64 digits * 16 digits
    int1_64 = random.randint(1e63, 1e64)
    int2_64 = random.randint(1e63, 1e64)
    
    int1 = 3141592653589793238462643383279502884197169399375105820974944592
    int2 = 2718281828459045235360287471352662497757247093699959574966967627
    
    print('----- 4 digits * 4 digits -----')
    print('int1 = ', int1_4)
    print('int2 = ', int2_4)
    print('Built-in function result: {}. \nTime spent = {}'.format(
            *evl(python_mul, int1_4, int2_4)))
    print('Self-imp function result: {}. \nTime spent = {}'.format(
            *evl(int_mul, int1_4, int2_4)))
    print('')
    
    print('----- 16 digits * 16 digits -----')
    print('int1 = ', int1_16)
    print('int2 = ', int2_16)
    print('Built-in function result: {}. \nTime spent = {}'.format(
            *evl(python_mul, int1_16, int2_16)))
    print('Self-imp function result: {}. \nTime spent = {}'.format(
            *evl(int_mul, int1_16, int2_16)))
    print('')
    
    print('----- 64 digits * 64 digits -----')
    print('int1 = ', int1_64)
    print('int2 = ', int2_64)
    print('Built-in function result: {}. \nTime spent = {}'.format(
            *evl(python_mul, int1_64, int2_64)))
    print('Self-imp function result: {}. \nTime spent = {}'.format(
            *evl(int_mul, int1_64, int2_64)))
    print('')
    
    print('----- Programming Assignment #1 -----')
    print('int1 = ', int1)
    print('int2 = ', int2)
    print('Built-in function result: {}. \nTime spent = {}'.format(
            *evl(python_mul, int1, int2)))
    print('Self-imp function result: {}. \nTime spent = {}'.format(
            *evl(int_mul, int1, int2)))
    print('')
"""
===== Results =====
    
----- 4 digits * 4 digits -----
int1 =  8220
int2 =  2914
Built-in function result: 23953080. 
Time spent = 0.0
Self-imp function result: 23953080. 
Time spent = 0.0

----- 16 digits * 16 digits -----
int1 =  1816443250374164
int2 =  9489599478642800
Built-in function result: 17237318921734899720426904619200. 
Time spent = 0.0
Self-imp function result: 17237318921734899720426904619200. 
Time spent = 0.0009970664978027344

----- 64 digits * 64 digits -----
int1 =  2104968846162103373550783363667652680876105070442868653658730193
int2 =  9106622569741617123023598256414743024930855512733701923471688264
Built-in function result: 19169156803062780553833643737303685851029158853411054207058261243539486089719694174798845780526550791659499570766564832180554952. 
Time spent = 0.0
Self-imp function result: 19169156803062780553833643737303685851029158853411054207058261243539486089719694174798845780526550791659499570766564832180554952. 
Time spent = 0.008986949920654297

----- Programming Assignment #1 -----
int1 =  3141592653589793238462643383279502884197169399375105820974944592
int2 =  2718281828459045235360287471352662497757247093699959574966967627
Built-in function result: 8539734222673567065463550869546574495034888535765114961879601127067743044893204848617875072216249073013374895871952806582723184. 
Time spent = 0.0
Self-imp function result: 8539734222673567065463550869546574495034888535765114961879601127067743044893204848617875072216249073013374895871952806582723184. 
Time spent = 0.0056438446044921875
    
"""