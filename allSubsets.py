def permutation(a):
    bits = [0] * len(a)
    permutationHelper(a, bits, 0)

def permutationHelper(a, bits, i):
    if i == len(a):
        print([a[i] for i,b in enumerate(bits) if b])
        return

    permutationHelper(a, [1 if index == i else v for index,v in enumerate(bits)], i + 1)
    permutationHelper(a, [0 if index == i else v for index,v in enumerate(bits)], i + 1)

lower = 1
upper = 3
startSet = [i for i in range(lower, upper + 1)]
permutation(startSet)