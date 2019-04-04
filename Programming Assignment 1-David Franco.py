# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 21:18:07 2019

@author: David Franco
CECS-229 Programming Assignment 1
"""


def main():

    #part 1
    seconds_in_decade = 10 * 365 * 24 * 60 * 60
    
    #part 2
    remainder_with_mod = 5789248 % 14
    
    #part 3
    remainder_without_mod = 5789248 - ((5789248 // 14) * 14) 
    
    #part 4
    {(x**3) - 1 for x in {2,4,6,8,10}}
    
    #part 5
    M = [1,2,3,4,5]
    [(x**2) - (x-1) for x in M]
    print("hello")

main()