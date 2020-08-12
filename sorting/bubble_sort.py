'''
----- Bubble Sort Algorithm ------

Author:http://github.com/rajashreey841
'''

import os
import sys

def bubbleSort(arr): 
    n = len(arr) 
    for i in range(n-1):
        swap = True
        for j in range(0, n-i-1):
            if arr[j + 1] < arr[j]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap = False
        if swap:
            return
 	
if __name__ == "__main__":
		a = input("Enter the integer \t")
		li = []
		liStr = a.split(",")
		for a in liStr:
			li.append(int(a))
		print("Input \t",li)
		bubbleSort(li)
		print("Sorted array is:",li)
		



