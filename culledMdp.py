import random
from itertools import combinations_with_replacement

MAX_BUY = 3
MAX_STORE = 4
GAMMA = 0.95    # Discount factor
LIMIT = 1    # Iteration limit

P_C = [[0.3, 0.2, 0.2, 0.1, 0.2],
       [0.3, 0.2, 0.2, 0.1, 0.2],
       [0.3, 0.2, 0.2, 0.1, 0.2],
       [0.3, 0.2, 0.2, 0.1, 0.2],
       [0.3, 0.2, 0.2, 0.1, 0.2]]

P_S = [[0.2, 0.2, 0.2, 0.2, 0.2],
       [0.2, 0.2, 0.2, 0.1, 0.3],
       [0.2, 0.2, 0.2, 0.1, 0.3],
       [0.2, 0.2, 0.2, 0.1, 0.3],
       [0.2, 0.2, 0.2, 0.1, 0.3]]

P = [P_C, P_S]

def getStates():
    for c in combinations_with_replacement(range(MAX_STORE + 1), 2):
        if sum(c) > MAX_STORE: continue
        yield(c)

def getActions(s):
    for c in combinations_with_replacement(range(MAX_BUY + 1), 2):
        if sum(c) > MAX_BUY: continue
        if sum(c) + sum(s) > MAX_STORE: continue
        yield(c)

def R(s, a):
    r = 0
    for i in range(len(s)):
        state, action = s[i], a[i]
        funds = state + action
        r +=   1 * sum([min(j, funds) * P[i][funds][j]        for j in range(1,         MAX_STORE + 1)])
        r -= 0.5 * sum([(j - state - action) * P[i][funds][j] for j in range(funds + 1, MAX_STORE + 1)])
    return r

def T(s, a, s_p):
    t = 1
    for i in range(len(s)):
        state, action, nextState = s[i], a[i], s_p[i]
        funds = state + action

        if nextState > funds:
            t *= 0
        elif nextState == 0:
            t *= sum([P[i][funds][j] for j in range(funds, MAX_STORE + 1)])
        else:
            t *= P[i][funds][funds - nextState]
    return t

def Q(s, a, V_t):
    return R(s, a) + GAMMA * sum([T(s, a, s_p) * V_t[s_p][0] for s_p in getStates()])

# Returns the best value and its action
def V(s, V_t):
    return max([(Q(s, a, V_t), a) for a in getActions(s)], key=lambda v:v[0])

def valueIteration():
    V_t = {s: [0, 0, None] for s in getStates()}
    for _ in range(LIMIT):
        # Update new values
        for s in getStates():
            V_t[s][1:] = V(s, V_t)
            print('_V:', s, *V_t[s])

        # Update old values
        for s in getStates():
            V_t[s][0] = V_t[s][1]

def policyIteration():
    V_t = {(0,0): [0, 0, [0,3]],
           (0,1): [0, 0, [0,2]],
           (0,2): [0, 0, [0,2]],
           (0,3): [0, 0, [0,1]],
           (0,4): [0, 0, [0,0]],
           (1,0): [0, 0, [0,3]],
           (1,1): [0, 0, [1,0]],
           (1,2): [0, 0, [1,0]],
           (1,3): [0, 0, [0,0]],
           (2,0): [0, 0, [0,1]],
           (2,1): [0, 0, [1,0]],
           (2,2): [0, 0, [0,0]],
           (3,0): [0, 0, [1,0]],
           (3,1): [0, 0, [0,0]],
           (4,0): [0, 0, [0,0]]}
    # V_t = {s: [0, 0, random.choice(list(getActions(s)))] for s in getStates()}
    for _ in range(LIMIT):
        # Estimate policy
        for s in getStates():
            V_t[s][1] = Q(s, V_t[s][2], V_t)

        # Improve policy
        for s in getStates():
            _, V_t[s][2] = V(s, V_t)
            print('_V:', s, *V_t[s])

        # Update old values
        for s in getStates():
            V_t[s][0] = V_t[s][1]

valueIteration()