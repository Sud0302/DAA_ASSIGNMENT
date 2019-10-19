## Design And Analysis of Algorithms Assignment

Problem defination : Given a string and pattern. Design pattern search algorithm which search the pattern exactly in the string or any permutation of pattern in the string.

## Getting Started

Well before moving towards the code let us understand this part of the problem definition:-
#### “will search the pattern exactly in the string or any Permutation of pattern in the string.”
So in order to understand "permutations of pattern in the String" , we need to be familiar with a concept called as ANAGRAMS.
Anagrams refer to those words which have the same alphabets ( also same number of alphabets) arranged in different order, 
for example : fried & fired, silent & listen are anagrams of each other.
So basically in this program we need to consider a particular check as successful if the pattern or any other pattern made by the permutations of the alphabets in the pattern is found.


## Approach 

Here we can use a simple meathod to find if a match has been found. We can store the frequencies of the ASCII values of all alphabets in pattern in a count array (lets say A[]), and compare it with the frequency array of ASCII values of the alphabets in the window on the String. If we find that the two values are equal, we have a match.

The easy approach to implement this is to use two count arrays:
1) The first count array stores the frequencies of characters in the given pattern.

2) The second count array stores frequencies of characters in current window of text.

3) Store counts of frequencies of pattern in first count array countP[]. Also store counts of frequencies of characters in first window of text in array countTW[].
 
2) Once we have the arrays , we will run a loop over the textv(considered in windows of size of the      pattern).
   a) If the two count arrays are identical, we found an occurrence.
   b) Increment count of current character of text in countTW[].
   c) Decrement count of first character in previous window in countWT[].
3) The last window is not checked by above loop, so explicitly check it.

## Understanding the code

The code is divided into various sections. Ill suggest that you keep this file open with you as you attempt to understand the code

Section 1: Here we declare MAX = 256 ,as we have maximum 256 possible characters in ASCII.

Section 2: Here we have written the logic for comparison, we run a loop till MAx , and if we find that somewhere the values do not march then we return a flase. Else we return true.

Section 3: In the third section we initialise the arrays and make all the entries inside the arrays as 0.

Section 4: In this section, we creare the freqency arrays. The " ord(pat[i]) " function returns the ASCII value of the character at index "i" in the pattern array.
So here we fill up the required values in the frequency arrays.

Section 5: Now we compare the arrays created in section 4, and notify if we find a match.

Section 6: Add next element to the window(the part of string into consideration).

Section 7: Remove the first element in the window(the part of string into consideration).

Section 8: Explicitly comparing the last window with the pattern.

Section 9: Giving inputs and calling the search funciton.

## Built With

SPYDER IDE: An open source cross-platform integrated development environment (IDE) for scientific programming in the Python language.
