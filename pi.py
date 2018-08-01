from math import gcd, sqrt
from random import randint

NUM_TESTS = 1000
LOWER_RANDOM = 0
UPPER_RANDOM = 100000

def get_pi_estimate():
    coprime_count = 0
    for _ in range(NUM_TESTS):
        random_one = randint(LOWER_RANDOM, UPPER_RANDOM)
        random_two = randint(LOWER_RANDOM, UPPER_RANDOM)
        coprime_count += gcd(random_one, random_two) == 1
    print(sqrt(6 / (coprime_count / NUM_TESTS)))

if __name__ == '__main__':
    get_pi_estimate()
