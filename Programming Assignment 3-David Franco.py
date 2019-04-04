# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 22:00:15 2019

@author: David Franco

    Chinese Remiander Theorem 

"""
import math

def main():
    #a mod m
    aList = [] #holds all the a vals
    mList = [] #holds all the m vals
    mLit = 1 #val of all ms multiplied
    mBigList = [] #holds vals of little m / a(n)
    mBig = 1 #val of little m / a(n)
    yList = [] #holds all the values of y(n)
    yVal = 1 #holds val of y(n)
    comboList = [] #holds val of a(n)*m(n)*y(n)
    
    aInput = input("Enter number for a or nothing when done: ")
    aList.append(aInput)
    
    while(aInput != ""):
        aInput = input("Enter number for a or nothing when done: ")
        if(aInput == ""):
            break
        aList.append(aInput)  
        
    aList = list(map(int,aList)) # list to int
    
    mInput = input("Enter number for m or nothing when done: ")
    mList.append(mInput)
    
    while(mInput != ""):
        mInput = input("Enter number for m or nothing when done: ")
        if(mInput == ""):
            break
        mList.append(mInput)  
        
    mList = list(map(int,mList)) #list to int
    
    #check if mList is pairwise relatively prime
    prime = relativelyPrime(mList) 
    
    #if not prime then display message, program over
    if(prime == False):
        print("Cannot proceed, mList input is not pairwise relatively prime")
        
    else:
        #multiply all ms
        for x in mList:
            mLit *= x
            
        #get big M val
        for y in mList:
            mBig = mLit / y
            mBig = int(mBig)
            mBigList.append(mBig)
            
        a = 0
        mVal = 0 #little m(a) val
        mBigVal = 0 #big M(a) val
        while a < len(mList):
            mBigVal = mBigList[a] #gets index val
            mVal = mList[a] #gets index val
            mCountVal = 1 #reset back to 1
            #max val of y(a) is up to little m val
            while mCountVal < mVal: #max repetition is m val
                
                yVal = ((mBigVal * mCountVal) % mVal) 
                
                if (yVal == 1): #mod is equal to 1
                    yList.append(mCountVal) #add to yList
                    break #from mCountVal < mVal
                mCountVal +=1 #inc mCountVal

            a+=1 #increment a
            
        b = 0
        aVal = 0 #a(b) val
        mBigVal1 = 0 #M(b) val
        yVal = 0 #y(b) val
        comboVal = 0 # val of a(b)*M(b)*y(b)
        while b < len(mList):
            aVal = aList[b]
            mBigVal1 = mBigList[b]
            yVal = yList[b]
            comboVal = aVal * mBigVal1 * yVal
            #add the vals into a list
            comboList.append(comboVal)
            b +=1
        megVal = 0 #val of all comboVal added
        for some in comboList:
            megVal += some #add all val in the comboList
        #final answer    
        megVal = megVal % mLit        
        
        print(megVal)
          

#from programming assignment #2    
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
                #print("Not pairwise relatively prime")
                return False
                minCounter = True
                megCounter = False
                break
            

            y+=1
        if(minCounter):
            break
        i+=1 #changes every time x changes, which is after y iterates
        y= i + 1 #to start one element ahead of x
        
    if(megCounter):
        #print("Pairwise relatively prime")    
        return True
    
    
main()   