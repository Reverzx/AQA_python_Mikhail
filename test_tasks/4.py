def plus_one(d):
    n = len(d)
    for i in range(n - 1, -1, -1):
        if d[i] < 9:
            d[i] += 1
            return d
        d[i] = 0
    return [1] + d


print(plus_one([9]))
print(plus_one([1, 2, 3]))
print(plus_one([1, 1, 9]))
print(plus_one([9, 9, 9]))
assert plus_one([9]) == [1, 0]
assert plus_one([1, 2, 3]) == [1, 2, 4]
assert plus_one([1, 1, 9]) == [1, 2, 0]
assert plus_one([9, 9, 9]) == [1, 0, 0, 0]
