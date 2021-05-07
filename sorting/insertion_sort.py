'''
----- Insertion Sort Algorithm ------

Author:http://github.com/rajashreey841

'''

import os
import sys

def insertionsort(array):
    for i in range(1,len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array

if __name__ == "__main__":
    lst = []
    n = int(input("Enter number of elements : "))
    for i in range(0, n):
        a = int(input())
        lst.append(a) 
    print("Result : ",insertionsort(lst))









