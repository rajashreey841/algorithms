'''
----- Selection Sort Algorithm ------

Author:http://github.com/rajashreey841

'''

import os
import sys

def selectionsort(array):
    for i in range(len(array)):
        min = i
        for j in range(i+1,len(array)):
            if  array[min] >array[j]:
                min = j
        array[i],array[min] = array[min],array[i]
    return array

if __name__ == "__main__":
    lst = []
    n = int(input("Enter number of elements : "))
    for i in range(0, n):
        a = int(input())
        lst.append(a) 
    print("Result : ",selectionsort(lst))
