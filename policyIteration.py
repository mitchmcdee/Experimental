import random

MAX_BUY = 3
MAX_STORE = 4
GAMMA = 0.95 # Discount factor
LIMIT = 2    # Iteration limit

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

def getStates():
    for s_c in range(MAX_STORE + 1):
        for s_s in range(MAX_STORE + 1):
            if s_c + s_s > MAX_STORE: continue
            yield(s_c, s_s)

def getTransitionStates(s, a):
    s_c, s_s = s
    a_c, a_s = a
    for s_p_c in range(s_c + a_c + 1):
        for s_p_s in range(s_s + a_s + 1):
            yield(s_p_c, s_p_s)

def getActions(s):
    s_c, s_s = s
    for a_c in range(MAX_BUY + 1):
        for a_s in range(MAX_BUY + 1):
            if a_c + a_s > MAX_BUY: continue
            if s_c + s_s + a_c + a_s > MAX_STORE: continue
            yield(a_c, a_s)

def R(s, a):
    s_c, s_s = s
    a_c, a_s = a
    
    r_c =    1 * sum([min(i, s_c + a_c) * P_C[s_c + a_c][i] for i in range(1,             MAX_STORE + 1)])
    r_c -= 0.5 * sum([(i - s_c - a_c)   * P_C[s_c + a_c][i] for i in range(s_c + a_c + 1, MAX_STORE + 1)])

    r_s =    1 * sum([min(i, s_s + a_s) * P_S[s_s + a_s][i] for i in range(1,             MAX_STORE + 1)])
    r_s -= 0.5 * sum([(i - s_s - a_s)   * P_S[s_s + a_s][i] for i in range(s_s + a_s + 1, MAX_STORE + 1)])

    return r_c + r_s

def T(s, a, s_p):
    s_c, s_s = s
    a_c, a_s = a
    s_p_c, s_p_s = s_p

    if s_p_c > s_c + a_c:
        t_c = 0
    elif 0 < s_p_c <= s_c + a_c:
        t_c = P_C[s_c + a_c][s_c + a_c - s_p_c]
    elif s_p_c == 0:
        t_c = sum([P_C[s_c + a_c][i] for i in range(s_c + a_c, MAX_STORE + 1)])

    if s_p_s > s_s + a_s:
        t_s = 0
    elif 0 < s_p_s <= s_s + a_s:
        t_s = P_S[s_s + a_s][s_s + a_s - s_p_s]
    elif s_p_s == 0:
        t_s = sum([P_S[s_s + a_s][i] for i in range(s_s + a_s, MAX_STORE + 1)])

    return t_c * t_s

def V_p(s, p):
    return R(s, p) + GAMMA * sum([T(s, p, s_p) * V_t[s_p][0] for s_p in getTransitionStates(s, p)])

def V_a(s):
    maxi = (0, None)
    for a in getActions(s):
        locali = V_p(s, a)
        if locali > maxi[0]:
            maxi = (locali, a)
    return maxi[1]

# V_t = {(0,0): [0, 0, [0,3]],
#        (0,1): [0, 0, [0,2]],
#        (0,2): [0, 0, [0,2]],
#        (0,3): [0, 0, [0,1]],
#        (0,4): [0, 0, [0,0]],
#        (1,0): [0, 0, [0,3]],
#        (1,1): [0, 0, [1,0]],
#        (1,2): [0, 0, [1,0]],
#        (1,3): [0, 0, [0,0]],
#        (2,0): [0, 0, [0,1]],
#        (2,1): [0, 0, [1,0]],
#        (2,2): [0, 0, [0,0]],
#        (3,0): [0, 0, [1,0]],
#        (3,1): [0, 0, [0,0]],
#        (4,0): [0, 0, [0,0]]}
V_t = {s: [0, 0, random.choice(list(getActions(s)))] for s in getStates()}
for _ in range(LIMIT):
    # Estimate policy
    for s in getStates():
        V_t[s][1] = V_p(s, V_t[s][2])
        print('_V:', s, *V_t[s])

    # Improve policy
    for s in getStates():
        V_t[s][2] = V_a(s)

    # Update old values
    for s in getStates():
        V_t[s][0] = V_t[s][1]