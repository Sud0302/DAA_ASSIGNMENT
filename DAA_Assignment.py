# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 00:40:22 2019

@author: sudha
"""

# Python program to search all 
# anagrams of a pattern in a text 
#Section 1.  
MAX=256 
#Section 2.  
def compare(arr1, arr2): 
    for i in range(MAX): 
        if arr1[i] != arr2[i]: 
            return False
    return True

def search(pat, txt): 
#Section 3.
    X = len(pat) 
    Y = len(txt) 

    patFreq = [0]*MAX
    txtFreq = [0]*MAX
#Section 4.  
    for i in range(X): 
        (patFreq[ord(pat[i]) ]) += 1
        (txtFreq[ord(txt[i]) ]) += 1
  
#Section 5.
    for i in range(X,Y): 
  
        if compare(patFreq, txtFreq): 
            print("The pattern(or it's anagram) is found at", (i-X)) 
  
#Section 6.
        (txtFreq[ ord(txt[i]) ]) += 1
#Section 7.  
        (txtFreq[ ord(txt[i-X]) ]) -= 1
      
#Section 8.    
    if compare(patFreq, txtFreq): 
        print("The pattern(or it's anagram) is found at", Y-X) 
#Section 9.                 
txt = "qwerwerqerqwrqwe"
pat = "qwer"       
search(pat, txt)    