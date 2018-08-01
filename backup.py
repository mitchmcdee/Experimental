NUM_VENTURES = 2
self.maxAdditional = 3
self.maxFunds = 3
GAMMA = 0.975
self.salePrices = [2, 1]

P = [[[0.1, 0.5, 0.2, 0.2],
      [0.1, 0.6, 0.2, 0.1],
      [0.2, 0.3, 0.3, 0.2],
      [0.2, 0.3, 0.2, 0.3]],

     [[0.1, 0.5, 0.2, 0.2],
      [0.1, 0.6, 0.2, 0.1],
      [0.2, 0.3, 0.3, 0.2],
      [0.2, 0.3, 0.2, 0.3]]]

# NUM_VENTURES = 3
# self.maxAdditional = 5
# self.maxFunds = 8
# GAMMA = 0.975
# self.salePrices = [3, 2, 3]

# P =[[[0.2, 0.2, 0.1, 0.0, 0.1, 0.1, 0.1, 0.1, 0.1],
#      [0.2, 0.1, 0.2, 0.1, 0.1, 0.1, 0.1, 0.0, 0.1],
#      [0.1, 0.2, 0.1, 0.1, 0.2, 0.1, 0.0, 0.1, 0.1],
#      [0.1, 0.1, 0.2, 0.0, 0.1, 0.2, 0.1, 0.1, 0.1],
#      [0.2, 0.1, 0.0, 0.1, 0.1, 0.1, 0.2, 0.1, 0.1],
#      [0.1, 0.2, 0.1, 0.1, 0.0, 0.1, 0.2, 0.1, 0.1],
#      [0.1, 0.0, 0.1, 0.1, 0.2, 0.1, 0.2, 0.1, 0.1],
#      [0.1, 0.1, 0.0, 0.1, 0.1, 0.2, 0.1, 0.2, 0.1],
#      [0.1, 0.0, 0.1, 0.1, 0.2, 0.1, 0.1, 0.1, 0.2]],

#     [[0.3, 0.1, 0.1, 0.1, 0.1, 0.1, 0.0, 0.1, 0.1],
#      [0.15, 0.15, 0.1, 0.2, 0.1, 0.0, 0.1, 0.1, 0.1],
#      [0.1, 0.15, 0.15, 0.2, 0.0, 0.1, 0.1, 0.1, 0.1],
#      [0.1, 0.15, 0.0, 0.1, 0.15, 0.2, 0.1, 0.1, 0.1],
#      [0.15, 0.1, 0.1, 0.1, 0.1, 0.1, 0.15, 0.1, 0.1],
#      [0.0, 0.1, 0.1, 0.1, 0.1, 0.1, 0.3, 0.1, 0.1],
#      [0.1, 0.1, 0.0, 0.1, 0.15, 0.1, 0.1, 0.25, 0.1],
#      [0.0, 0.1, 0.1, 0.1, 0.1, 0.2, 0.12, 0.13, 0.15],
#      [0.1, 0.0, 0.0, 0.1, 0.1, 0.0, 0.2, 0.3, 0.2]],

#     [[0.1, 0.2, 0.1, 0.0, 0.1, 0.2, 0.1, 0.1, 0.1],
#      [0.2, 0.1, 0.2, 0.1, 0.1, 0.1, 0.1, 0.0, 0.1],
#      [0.1, 0.2, 0.1, 0.1, 0.2, 0.1, 0.0, 0.1, 0.1],
#      [0.2, 0.1, 0.2, 0.0, 0.0, 0.2, 0.1, 0.1, 0.1],
#      [0.3, 0.1, 0.0, 0.1, 0.1, 0.1, 0.2, 0.0, 0.1],
#      [0.1, 0.2, 0.1, 0.1, 0.0, 0.1, 0.2, 0.1, 0.1],
#      [0.2, 0.0, 0.1, 0.1, 0.2, 0.1, 0.2, 0.1, 0.0],
#      [0.1, 0.1, 0.0, 0.1, 0.1, 0.2, 0.1, 0.2, 0.1],
#      [0.0, 0.0, 0.1, 0.1, 0.2, 0.2, 0.1, 0.1, 0.2]]]

def getStates():
    for s in product(range(self.maxFunds + 1), repeat=self.numVentures):
        if sum(s) > self.maxFunds: continue
        yield(s)

def getActions(s):
    for a in product(range(self.maxAdditional + 1), repeat=self.numVentures):
        if sum(a) > self.maxAdditional: continue
        if sum(a) + sum(s) > self.maxFunds: continue
        yield(a)

def R(s, a):
    r = 0
    for i in range(len(s)):
        state, action = s[i], a[i]
        funds = state + action

        for j in range(self.maxFunds + 1):
            sold = min(j, funds)
            missed = j - sold
            r += sold   * 0.6  * (self.salePrices[i] - 1) * P[i][funds][sold]
            r -= missed * 0.25 *  self.salePrices[i]      * P[i][funds][missed]
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
    startTime = time.time()

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

    totalTime = time.time() - startTime
    print(f'Value Iteration converged after {count} iterations ({totalTime:.4f}s), developing the optimal policy:')
    [print(s, '->', V_t[s][-1]) for s in getStates()]

def policyIteration():
    count = 0
    converged = False
    startTime = time.time()

    V_t = {s: [0, choice(list(getActions(s)))] for s in getStates()}
    while not converged:
        count += 1

        # Evaluate policy
        for s in getStates():
            V_t[s][0] = Q(s, V_t[s][1], V_t)

        # Improve policy
        converged = True
        V_t_p = {**V_t}
        for s in getStates():
            V_t[s] = list(V(s, V_t))
            if V_t[s] != V_t_p[s]:
                converged = False
            # print('_V:', s, *V_t[s])
            # print(s, '->', V_t[s][-1])

    totalTime = time.time() - startTime
    print(f'Policy Iteration converged after {count} iterations ({totalTime:.4f}s), developing the optimal policy:')
    [print(s, '->', V_t[s][-1]) for s in getStates()]

valueIteration()
print()
policyIteration()