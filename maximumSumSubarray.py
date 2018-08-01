def getMaximumSumSubarray(a):
    if len(a) == 0:
        return 0

    isAllPositive = a[0] >= 0
    isAllNegative = a[0] < 0
    totalSums = [a[0]]
    for i in range(1, len(a)):
        v = a[i]
        isAllPositive &= v >= 0
        isAllNegative &= v < 0
        totalSums.append(v + totalSums[-1])

    if isAllPositive:
        return totalSums[-1]
    elif isAllNegative:
        return max(a)
    else:
        return max(totalSums) - min(totalSums)

assert(6 == getMaximumSumSubarray([1, 2, 3]))
assert(-1 == getMaximumSumSubarray([-3, -4, -1]))
assert(1 == getMaximumSumSubarray([-1, 0, 1]))
assert(10 == getMaximumSumSubarray([-1, 3, -5, 10]))
assert(11 == getMaximumSumSubarray([-100, 6, -5, 10]))
print('Passes all tests!')