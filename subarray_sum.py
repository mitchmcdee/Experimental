def get_subarray_sum_to_target_indices(target, nums):
    sums = {0: [0]}
    cumulative_sum = 0
    for i, num in enumerate(nums):
        cumulative_sum += num
        if cumulative_sum not in sums:
            sums[cumulative_sum] = []
        sums[cumulative_sum].append(i + 1)
    return [sorted([i, j])
            for end in sums
            for j in sums[end]
            for i in sums.get(end - target, [])]

target = int(input())
nums = list(map(int, input().strip().split()))
print(get_subarray_sum_to_target_indices(target, nums))
