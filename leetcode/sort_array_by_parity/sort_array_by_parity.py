def sort_array_by_parity(A):
    B = []
    for i in A:
        if i % 2 == 0:
            B = [i] + B
        else:
            B = B + [i]
    return B