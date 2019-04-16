# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 21:32:06 2019

@author: David Franco

    RSA Encryption

"""


def main():
    
    #modulus, product of two primes
    n = int(input("Enter n "))
    
    #exponential value
    e = int(input("Enter e "))
    
    #text message
    mes = str(input("Enter message "))
    
    if(mes == ""):
        print("Message length need to be greater than 0")
    else:
       RSAencrypt(n,e,mes)     
    
    
def RSAencrypt(n,e,mes):
    #alphabet list
    charList = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O",
                    "P","Q","R","S","T","U","V","W","X","Y","Z"]
    
    #number list to correspond with the alphabet
    numList = ["00","01","02","03","04","05","06","07","08","09","10","11",
     "12","13","14","15","16","17","18","19","20","21","22","23","24","25"]
    
    someList = [] #numbers in blocks
    someList1 = "" #string of numbers
    
    
    #determine how many number of digits for the blocks
    if 25 < n <2525:
        div = 2 #two digits needed
    if 2525 < n < 252525:
        div = 4 #4 digits needed
    if 252525 < n < 25252525:
        div = 6 #6 digits needed
    if 25252525 < n < 2525252525:
        div = 8 #8 digits needed
    if 2525252525 < n < 252525252525:
        div = 10 #10 digits neede
    
    for char in mes: #for every character in message   
        i = 0 #for numList
        for char1 in charList: #for every letter in the alphabet
            #when alphabet char matches char from message
            if char1 == char:
                #add the corresponding letter number 
                someList1 += numList[i]
                #check length of string
                length = len(someList1)
                #since we divide the block based on div, wait for string to 
                #have length div. 
                if length == div:
                    #add string chars up to length div
                    someList.append(someList1)
                    #string empty, add number and wait until string reaches
                    #length of div
                    someList1 = ""
                
            i+=1 #trasverse through the entire numList until char is found
       
    #if string is not empty, then the block needs to be completed
    if someList1 != "":
        counter = True #for while loop
        while(counter):
            someList1 += "23" #add value of X
            if len(someList1) == div: #if string equals div
                someList.append(someList1) #add new block to list
                counter = False #to exit loop
    #list that holds final solution        
    finList = []
        
    #for every block of code  
    for M in someList:
            M = int(M) #to int
            C = pow(M,e) % n #modulos remiander
            C = str(C) #to string
            while(len(C) != div):
                #add 0 until block matches div
                C = "0" + C
            finList.append(C)
   #print final solution 
    print(finList)

main()