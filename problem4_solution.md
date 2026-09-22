## Problem 4

If we split our input into `m` parts where `m > 0` then the depth of recursion is going to be `log_m(n) ~ log n` and on each level we are going to do `O(n)` amount of job. So the time complexity still remains `O(nlogn)`

The depth of our recursion becomes `log_m(n) ~ log n` at each layer we store `m` lists with `n` elements in total. So we have `O(logn + n) ~ O(n)` space complexity.