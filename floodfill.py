import math

# init sizes
width = 30
height = 30 

# init empty grid
g = [['.']*width for i in range(height)]

# init circle dimensions (radius and center point)
r = min(height,width)//2.5      # radius
center = (width//2, height//2)  # center of grid

# create empty circlular border in the grid
for j in range(len(g)):
    for i in range(len(g[j])):
        if int(math.sqrt(abs(i-center[0])**2 + abs(j-center[1])**2)) == r:
            g[j][i] = 'O'

# print out grid before
print('Before:')
for i in range(len(g)):
    print(''.join(g[i]))

# add some spacing
print('\n\n')

# add root (center of grid) to stack and visited
root = center
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

        # check valid neighbour to visit
        if g[y][x] == 'O' or neighbour in visited:
            continue

        # check within bounds
        if x < 0 or y < 0 or x >= width or y >= height:
            continue

        # add neighbour to stack and visited set
        visited.add(neighbour)
        stack.append(neighbour)

    # fill node
    g[node[1]][node[0]] = 'O'

# print out grid after
print('After:')
for i in range(len(g)):
    print(' '.join(g[i]))