#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Linear O(n), at all times there is one operation performed for each iteration while a < n^3


b) Linearithmic O(n log n), the loop is justified as n while the while loop within each iteration is an extra step which results in log n.


c) O(n), Only one operation is being performed (+2) for each recursion

## Exercise II

A binary search approach can lead to the least amount of eggs used for this test.

def binary_search(arr, n):
  low = 0
  high = len(arr)-1
  while low <= high:
    middle = (low+high)/2
    if n < arr[middle]:
      high = middle-1
    elif n > arr[middle]:
      low = middle+1
    else: 
      return middle
