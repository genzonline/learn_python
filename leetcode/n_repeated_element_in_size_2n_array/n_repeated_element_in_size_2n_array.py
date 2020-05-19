def repeatedNTimes(self, A: List[int]) -> int:
    B = set([])
    for i in A:
        if i in B:
            return i
        else:
            B.add(i)