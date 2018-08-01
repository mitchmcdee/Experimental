def canEscape(a):
    goal = len(a)
    for i in reversed(range(len(a))):
        if i + a[i] >= goal:
            goal = i
    return goal == 0

print(canEscape([1, 1, 0, 2, 0, 1]))