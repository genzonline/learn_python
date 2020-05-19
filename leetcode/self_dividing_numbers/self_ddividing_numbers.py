def self_dividing_numbers(self, left, right):
    ans = []
    check = True
    for i in range(left, right + 1):
        for j in str(i):
            if int(j) == 0:
                check = False
            elif i % int(j) != 0:
                check = False
        if check == True:
            ans.append(i)
        else:
            check = True
    return ans