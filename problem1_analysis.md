## Problem 1:

### Selection Sort
Time : `O(n^2)` - on each element we iterate through the remaining list to find the minimum.

Space : `O(n)` - we make `n` calls for `selection sort` plus up to `n` calls for finding minimum.

#### Explanation:

`selection_sort` iterates through the list index by index via recursion.

For the current index `n`, `find_min` recursively scans the remaining list on the right to find the index of the minimum element.

The element at index `n` is swapped with the minimum element found.

The function then recursively calls itself on index `n + 1`.

### Insertion Sort
Time : `O(n^2)` - on each element we shift it left through the sorted section until it reaches its correct position.

Space : `O(n)` - we make `n` calls for `insertion_sort` plus up to `n` calls for shifting the element left.

#### Explanation:

`insertion_sort` iterates through the list index by index starting at index 1 via recursion.

For the current index `curr`, `insertion_sort` recursively compares the element with its left neighbor and swaps them if it is smaller.

The function then recursively calls itself on index `curr + 1`.


