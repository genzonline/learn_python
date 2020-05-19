def isMonotonic(A: List[int]) -> bool:
    typefound = False
    monotonic = True
    increasing = None
    count = 0
    tmp = None
    for i in A:
        if count == 0:
            pass
        elif count == 1:
            if i > tmp:
                typefound = True
                increasing = True
            elif i < tmp:
                typefound = True
                increasing = False
        else:
            if typefound:
                print(tmp, i, (increasing and i < tmp) or ((not increasing) and i > tmp))
                if (increasing and i < tmp) or ((not increasing) and i > tmp):
                    return False
            else:
                if i > tmp:
                    typefound = True
                    increasing = True
                elif i < tmp:
                    typefound = True
                    increasing = False
        count += 1
        tmp = i
        
    return True