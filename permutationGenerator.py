def permutations(a):
    if len(a) == 0:
        yield []

    for i,v in enumerate(a):
        remainder = a[:i] + a[i + 1:]
        for p in permutations(remainder):
            yield [v] + p

a = [1, 2, 3]
[print(permutation) for permutation in permutations(a)]