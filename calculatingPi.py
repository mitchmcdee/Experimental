from math import gcd, sqrt
from random import randrange

def coprime(a, b):
    return gcd(a, b) == 1

NUM_TRIALS = 1000000
RAND_RANGE = 1000000

numCoprime = 0
for i in range(NUM_TRIALS):

	num1 = randrange(RAND_RANGE)
	num2 = randrange(RAND_RANGE)

	numCoprime += 1 if coprime(num1, num2) else 0

x = float(numCoprime) / NUM_TRIALS
pi = sqrt(6/x)

print(pi)