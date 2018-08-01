import random
import sys
from itertools import product

MAX_ADDITIONAL = 3
MAX_FUNDING = 3
GAMMA = 0.975    # Discount factor
LIMIT = 1      # Iteration limit
SALE_PRICE = [2, 1]

P = [[[0.1, 0.5, 0.2, 0.2],
      [0.1, 0.6, 0.2, 0.1],
      [0.2, 0.3, 0.3, 0.2],
      [0.2, 0.3, 0.2, 0.3]],

     [[0.1, 0.5, 0.2, 0.2],
      [0.1, 0.6, 0.2, 0.1],
      [0.2, 0.3, 0.3, 0.2],
      [0.2, 0.3, 0.2, 0.3]]]

def getStates():
    for s in product(range(MAX_FUNDING + 1), repeat=2):
        if sum(s) > MAX_FUNDING: continue
        yield(s)

def getActions(s):
    for a in product(range(MAX_ADDITIONAL + 1), repeat=2):
        if sum(a) > MAX_ADDITIONAL: continue
        if sum(a) + sum(s) > MAX_FUNDING: continue
        yield(a)

def R(s, a):
    r = 0
    for i in range(len(s)):
        state, action = s[i], a[i]
        funds = state + action

        for j in range(MAX_FUNDING + 1):
            sold = min(j, funds)
            missed = j - sold
            r += sold   * 0.6  * (SALE_PRICE[i] - 1) * P[i][funds][sold]
            r -= missed * 0.25 * SALE_PRICE[i]       * P[i][funds][missed]
    return r

def T(s, a, s_p):
    t = 1.0
    for i in range(len(s)):
        state, action, nextState = s[i], a[i], s_p[i]
        funds = state + action

        if nextState > funds:
            t *= 0
        else:
            t *= P[i][funds][funds - nextState]
    return t

def Q(s, a, V_t):
    return R(s, a) + GAMMA * sum([T(s, a, s_p) * V_t[s_p][0] for s_p in getStates()])

def V(s, V_t):
    return max([(Q(s, a, V_t), a) for a in getActions(s)], key=lambda v:v[0])

def valueIteration():
    count = 0
    delta = 1
    minDelta = sys.float_info.epsilon * (1 - GAMMA) / GAMMA

    V_t = {s: [0, None] for s in getStates()}
    while delta > minDelta:
        count += 1
        delta = 0
        V_t_p = {**V_t}
        for s in getStates():
            V_t[s] = V(s, V_t)
            delta = max(delta, abs(V_t[s][0] - V_t_p[s][0]))
            # print(f'{s}:', *V_t_p[s], *V_t[s])
            # print(s, '->', V_t[s][-1])

    print(f'converged after {count} iterations, developing the optimal policy:')
    [print(s, '->', V_t[s][-1]) for s in getStates()]

def policyIteration():
    V_t = {s: [0, 0, random.choice(list(getActions(s)))] for s in getStates()}
    for _ in range(LIMIT):
        # Estimate policy
        for s in getStates():
            V_t[s][1] = Q(s, V_t[s][2], V_t)

        # Improve policy
        for s in getStates():
            _, V_t[s][2] = V(s, V_t)
            # print('_V:', s, *V_t[s])
            print(s, '->', V_t[s][-1])

        # Update old values
        for s in getStates():
            V_t[s][0] = V_t[s][1]

valueIteration()
# policyIteration()
# print(T((1,1),(0,1),(1,0)))
# print(R((1,1),(0,1)))