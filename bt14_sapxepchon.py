# -*- coding: utf-8 -*-
"""BT14_SapXepChon

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LbppfYbTA3pNGQw_KgBU-FO8Q1ZJMk2f
"""

A = [64, 25, 12, 22, 11]
print('Mảng:',A) 
# Traverse through all array elements
for i in range(len(A)):
    # Find the minimum element in remaining 
    # unsorted array
    min_idx = i
    for j in range(i+1, len(A)):
        if A[min_idx] > A[j]:
            min_idx = j
              
    # Swap the found minimum element with 
    # the first element        
    A[i], A[min_idx] = A[min_idx], A[i]
  
# Driver code to test above
print ("Sorted array")
for i in range(len(A)):
    print("%d" %A[i]),