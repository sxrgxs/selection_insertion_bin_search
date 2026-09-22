def selection_sort(seq : list, n : int = 0) -> None:
    if len(seq) == 0:
        return
    if n == len(seq) - 1:
        return
    min_index = find_min(seq, n, n)
    seq[n], seq[min_index] = seq[min_index], seq[n]
    selection_sort(seq, n + 1)

def find_min(seq : list, curr : int, min_index : int) -> int:
    if curr == len(seq):
        return min_index
    if seq[curr] > seq[min_index]:
        return find_min(seq, curr + 1, min_index)
    return find_min(seq, curr + 1, curr)

def insertion_sort(seq: list, curr: int = 1, n: int = 1):
    if len(seq) == 0:
        return
    if curr == len(seq):
        return
    if seq[n] < seq[n-1]:
        seq[n], seq[n-1] = seq[n-1], seq[n]
        if n > 1:
            insertion_sort(seq, curr, n-1)
        else:
            insertion_sort(seq, curr+1, curr+1)
    else:
        insertion_sort(seq, curr+1, curr+1)

a = [-1 , 4, 5, -2,1, 3, 1, -10]

insertion_sort(a)

print(a)