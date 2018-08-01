from random import randint

a = [randint(1, 9) for i in range(randint(2, 10))]
print('Before:', ''.join(map(str, a)))

carry = False
for i in reversed(range(len(a))):
    sumi = a[i] + 1
    carry = True if sumi == 10 else False
    a[i] = sumi % 10
    if carry is False: break

if carry: a = [1] + a
print('After:', ''.join(map(str, a)))