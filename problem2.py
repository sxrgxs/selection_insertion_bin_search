def binary_search(seq, left, right):
    if left >= right:
        return left
    mid = (right + left) // 2
    if (seq[mid + 1] - seq[mid]) % 2 != 0:
        return binary_search(seq, mid + 1, right)
    return binary_search(seq, left, mid)

seq = [4, 1, 4, 9, 16, 22, 30, 38, 46]

print(binary_search(seq, 0, len(seq) - 1))