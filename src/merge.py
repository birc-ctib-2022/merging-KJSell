"""Code for merging two sorted lists."""


def merge(x: list[int], y: list[int]) -> list[int]:
    i, j = 0, 0
    z = []
    big_number = float('inf') #7
    x.append(big_number)
    y.append(big_number)
    while i < len(x) and j < len(y):
        if x[i] <= y[j]:
            z.append(x[i])
            i += 1
        else:
            z.append(y[j])
            j += 1
        print((i,j))
    z.remove(big_number)
    return z
print(merge([1, 2, 4, 6], [1, 3, 4, 5]))
