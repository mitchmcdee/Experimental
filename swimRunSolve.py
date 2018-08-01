from math import sqrt

n = int(input())

def getHyp(a, b):
    return sqrt(a**2 + b**2)

def getTime(guess, x, y_w, y_s, v_w, v_s):
    hyp_w = getHyp(guess, y_w)
    hyp_s = getHyp(x - guess, y_s)
    return hyp_w / v_w + hyp_s / v_s

def getTurningPoint(a):
    for i in range(1, len(a) - 1):
        if a[i - 1] < a[i] and a[i + 1] < a[i]:
            return i, 'inc'
        if a[i - 1] > a[i] and a[i + 1] > a[i]:
            return i, 'dec'
    return -1

for i in range(n):
    x, y_w, y_s, v_w, v_s = list(map(int, input().split()))

    # Sample 10
    samples = [getTime((x * i) / 10, x, y_w, y_s, v_w, v_s) for i in range(11)]
    turningPoint = getTurningPoint(samples)
    lower = (x * turningPoint) / 10
    upper = (x * (turningPoint + 1)) / 10
    print(lower, upper)


    # mini = (0, getTime(0, x, y_w, y_s, v_w, v_s))
    # for k in range(10):
    #     for i in range(mini[0], x, x // (10**k)):
    #         val = getTime(i, x, y_w, y_s, v_w, v_s)
    #         if val < mini[1]:
    #             mini = (i, val)
    #     print(mini)

