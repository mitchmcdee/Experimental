from random import random

def randomOrder(a):
    print(a)

    for i in reversed(range(1, len(a))):
        j = int(random() * (i + 1)) # Random floor
        a[i], a[j] = a[j], a[i]    # Random swap

    print(a)

randomOrder([3, 1, 9, 0, 2])