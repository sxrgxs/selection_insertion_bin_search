## Problem 2:

Time : `O(log n)` - on each step we take half of the length.

Space : `O(log n)` - recursion stack depth is proportional to the tree height `(log n)`.

#### Explanation:

`binary_search` checks the difference between `seq[mid]` and `seq[mid + 1]`.

If the step is odd the turning point is to the right so we recurse on the right half.

If the step is even either mid or lies to the left so we recurse on the left half including mid.

The base case left >= right converges on the turning point where the step first becomes even.

We also can think of it as a sequence of 0s and 1s like if the difference is odd then put 0 if difference is even then put 1 so in the example in the solution we get `[0,0,0,0,0,1,1,1,1]` which is monotonic so we can use bin search which is just going to converge `left` and `right` to the first occurence of `1`.