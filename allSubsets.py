def permTwo(a):
    bits = [0] * len(a)
    permTwoHelper(a, bits, 0)

def permTwoHelper(a, bits, i):
    if i == len(a):
        print([a[i] for i,b in enumerate(bits) if b])
        return

    permTwoHelper(a, [1 if index == i else v for index,v in enumerate(bits)], i + 1)
    permTwoHelper(a, [0 if index == i else v for index,v in enumerate(bits)], i + 1)

lower = 1
upper = 3
array = [i for i in range(lower, upper + 1)]
permTwo(array)