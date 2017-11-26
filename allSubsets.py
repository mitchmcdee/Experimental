def allSubsets(a):
    bits = [0] * len(a)
    allSubsetsHelper(a, bits, 0)

def allSubsetsHelper(a, bits, i):
    if i == len(a):
        print([a[i] for i,b in enumerate(bits) if b])
        return

    bits[i] = 0
    allSubsetsHelper(a, bits, i + 1)
    bits[i] = 1
    allSubsetsHelper(a, bits, i + 1)

lower = 1
upper = 3
startSet = [i for i in range(lower, upper + 1)]
allSubsets(startSet)