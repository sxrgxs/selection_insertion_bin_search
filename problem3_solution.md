## Problem 3:

List: [10,9,8,7,6,5,4,3,2,1]

For MergeSort there is no difference in which list we choose as it is stable and always does its job in `O(nlogn)`.

For QuickSort we chose this array as choosing the first element means that it will eventually create `O(n)` recursive calls (putting n-1, n-2, ... elements in the left) each level doing `O(n)` amount of job resulting in `O(n^2)` time complexity. 

For Insertion sort we chose this array because every new element is smaller than all previously sorted elements, meaning it has to shift each element all the way to the beginning.

### Illutstrations:

MergeSort: 

divide `[10, 9, 8, 7,6]` 
 
divide `[10, 9, 8]`

divide `[10, 9]` divide `[10]` divide `[9]` conquer `[9, 10]`

divide `[8]` conquer `[8, 9, 10]`

divide `[7, 6]` divide `[7]` divide `[6]` conquer `[6, 7]` 

conquer `[6, 7 ,8 ,9 ,10]`

divide `[5, 4, 3, 2, 1]`

divide `[5, 4, 3]`

divide `[5, 4]` divide `[5]`, divide `[4]`, conquer `[4, 5]`

divide `[3]` conquer `[3, 4, 5]`

divide `[2, 1]` divide `[2]`, divide `[1]`, conquer `[1, 2]`

conquer `[1, 2, 3, 4 ,5]`

conquer `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`

QuickSort:
Pivot = 10  Left: `[9, 8, 7, 6, 5, 4, 3, 2, 1]`, Right: []

Pivot = 9 Left: `[8, 7, 6, 5, 4, 3, 2, 1]`, Right: []

Pivot = 8 Left: `[7, 6, 5, 4, 3, 2, 1]`, Right: []

Pivot = 7 Left: `[6, 5, 4, 3, 2, 1]`, Right: []

Pivot = 6 Left: `[5, 4, 3, 2, 1]`, Right: []

Pivot = 5 Left: `[4, 3, 2, 1]`, Right: []

Pivot = 4 Left: `[3, 2, 1]`, Right: []

Pivot = 3 Left: `[2, 1]`, Right: []

Pivot = 2  Left: `[1]`, Right: []

`[1]` base case

and it will classify empty strings of right as base cases and conquer all of our calls each time combining our results.

InsertionSort:

Assume first element sorted

curr = 9: each time looks left swaps with left until the beginning `[9, 10, 8, 7, 6, 5, 4, 3, 2, 1]`

curr = 8: `[8, 9, 10, 7, 6, 5, 4, 3, 2, 1]`

curr = 7: `[7, 8, 9, 10, 6, 5, 4, 3, 2, 1]`

curr = 6: `[6, 7, 8, 9, 10, 5, 4, 3, 2, 1]`

curr = 5: `[5, 6, 7, 8, 9, 10, 4, 3, 2, 1]`

curr = 4: `[4, 5, 6, 7, 8, 9, 10, 3, 2, 1]`

curr = 3: `[3, 4, 5, 6, 7, 8, 9, 10, 2, 1]`

curr = 2: `[2, 3, 4, 5, 6, 7, 8, 9, 10, 1]`

curr = 1: `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`

## Reverse order

MergeSort: `O(nlogn)` as it is stable

QuickSort: `O(n^2)` now we put everything to the right and again `O(n)` depth `O(n)` amount of job on each layer result in `O(n^2)` time complexity

InsertionSort: `O(n)` as now we just do `n-1` comparings with no swaps.