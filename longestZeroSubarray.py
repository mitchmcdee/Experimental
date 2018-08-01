def getLongestZeroSubarray(a):
    longestZeroSum = -1
    totalSum = 0
    sums = {0:-1}
    for i, v in enumerate(a):
        totalSum += v
        if totalSum in sums:
            longestZeroSum = max(longestZeroSum, i - sums[totalSum])
        else:
            sums[totalSum] = i
    return longestZeroSum

assert(5 == getLongestZeroSubarray([15, -2, 2, -8, 1, 7, 10, 13]))
assert(4 == getLongestZeroSubarray([5, 3, 2, -10]))
assert(3 == getLongestZeroSubarray([1, 0, -1, 2]))
assert(-1 == getLongestZeroSubarray([1, 2, 3]))
print('Passes all tests!')