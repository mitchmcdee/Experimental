def num_ways(n, step_options):
    steps = [None] * n

    def num_ways_at_step(i):
        if i > n:
            return 0
        if i == n:
            return 1
        if i not in steps:
            steps[i] = sum(num_ways_at_step(i + j) for j in step_options)
        return steps[i]

    return num_ways_at_step(0)







def num_ways_v2(n, step_options):
    positions = n + 1
    steps = [0] * positions
    steps[positions - 1] = 1
    for position in reversed(range(positions)):
        for step in step_options:
            next_position = position + step
            if next_position >= positions:
                continue
            steps[position] += steps[next_position]
    return steps[0]







def main():
    print(num_ways(11, set([1, 2])))
    # print(num_ways_v2(50000, set([1, 2, 5])))

if __name__ == '__main__':
    main()