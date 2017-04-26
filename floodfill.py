# init sizes
width = 1000
height = 1000

# init empty grid
g = [['0']*width for i in range(height)]

# create diagonal border from top right down
for i in range(len(g)):
	g[i][width-i-1] = '1'

# print out grid before
print('Before:')
for i in range(len(g)):
	print(''.join(g[i]))

# add some spacing
print('\n\n')

# add root to stack and visited
root = (0,0)
visited = set(root)
stack = [root]

# directions of neighbours
directions = [(1,0), (0,1), (-1,0), (0,-1)]

# perform dfs
while len(stack) != 0:
	# get next node
	node = stack.pop()

	# check neighbours
	for direction in directions:
		x = node[0] + direction[0]
		y = node[1] + direction[1]
		neighbour = (x,y)

		# check valid neighbour
		if neighbour not in visited and x >= 0 and y >= 0 and x < width and y < height and g[y][x] == '0':
			visited.add(neighbour)
			stack.append(neighbour)

	# fill node
	g[node[1]][node[0]] = '1'

# print out grid after
print('After:')
for i in range(len(g)):
	print(''.join(g[i]))