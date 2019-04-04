# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 10:10:33 2019

@author: David Franco


"""

import math

def main():
    
    print("Assignment 1")
    input0 = input("Enter base: ") #base
    base = int(input0)
    input1 = input("Enter exponent: ") #exponent
    exp = int(input1)
    input2 = input("Enter divisor: ") #divisor
    div = int(input2)
    
    #part one of program assignment
    modulus(base,exp,div)
    
    numList = []
    
    print(" ")
    print("Assignment 2")

    
    input3 = input("Enter numbers or nothing when done ")
    #prime = int(input3) #values to go in list
    numList.append(input3)
    
    #to exit loop user input must hit enter with no number
    while(input3 != ""):
        
        
        input3 = input("Enter numbers or nothing when done ")
        #prime = int(input3)
        if input3 == "":
            break
        
        numList.append(input3)
     
    #all values in list to int type    
    numList = list(map(int,numList))
    
    #part 2 of assignment
    relativelyPrime(numList) #passing list
     
        

    
 #part 1 of assignment   
def modulus(base,exp,div):
    
    #holds vals of counter where a '1' appears
    #in the binary expression
    count = []
    #holds vals of modulus
    count0 = []
    #holds final vals of function
    count1 = []

    #change exponent to binary
    exp = bin(exp)
    
    #remove '0b' from binary expression
    exp = exp[2:] 
    
    #length of binary expression minus 1, we consider position 0
    counter = len(exp) - 1  
    
    #looking for '1' in binary expression
    for x in exp:
       if x == '1':
           #add position of '1' to count  
           count.append(counter) 
       #decrement i    
       counter-=1
    
    #length of binary expression   
    counter = len(exp) -1
    
    #double after ever iteration in while loop

    a = 1
    
    #while loop gets the mod value, up to the size of binary
    #expression, base exponent is double after iteration
    while(counter != -1):
       #modulus value 
       rem = (base**(a)) % div
       count0.append(rem)
       counter-=1
       a*=2
       
    #for formatting
    count.reverse()
    
    #for every position of '1' in the binary(count)
    #we get the value of the mod(count0) in that position
    #add it to the final solution(count1) in a list
    for y in count:
        count1.append(count0[y])

    
    print(count1)


#part 2 of assignment
def relativelyPrime(numList):

    #value of gcd 
    gcdVal = 0
    
    """
    gcd(x,y)
    i: this counter is responsible for the y value in the gcd.
    while x is a fixed element, y must iterate through the list starting
    from the position x + 1, in other words i tells y where in the list
    to start.
    """
    i = 0
    
    """
    y: the value that iterates through the list.
    starting position depends on i
    """
    y = 1
    
    """
    minCounter: used to break out of the for loop
    megCounter: determines if output will be pairwise/not-pairwise
    """
    minCounter = False
    megCounter = True
    
    """
    gcd(x,y)
    x can be considered the big loop, starting at element 0, it waits until
    y has iterated through the list (starting at y = i + 1) then moves on 
    to the next element until all possible gcds have been checked
    """
    for x in numList:
        while y < len(numList):      
            #get gcd of x,y
            gcdVal = math.gcd(x,numList[y])
            
            #if gcd does not equal 1 then the whole list of number is
            #not pairwise
            if gcdVal != 1:
                print("Not pairwise relatively prime")
                minCounter = True
                megCounter = False
                break
            

            y+=1
        if(minCounter):
            break
        i+=1 #changes every time x changes, which is after y iterates
        y= i + 1 #to start one element ahead of x
        
    if(megCounter):
        print("Pairwise relatively prime")
    
main()