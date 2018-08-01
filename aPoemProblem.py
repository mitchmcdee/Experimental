n = int(input())
m = int(input())

eMap = {}
dMap = {}
for i in range(n):
    a, b = input().split()
    eMap[a] = b
    dMap[b] = a

for i in range(m):
    mode, message = input().split()
    if mode == 'E':
        print(''.join([eMap[l] if l in eMap else l for l in message]))
    else:
        print(''.join([dMap[l] if l in dMap else l for l in message]))