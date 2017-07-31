def permutations_of_items_in_bins(items, items_per_bin, number_of_bins, pad='z'):
    # Convert items to a dictionary that tracks how many we have of each
    pile = {}
    for item in items:
        try:
            pile[item] += 1
        except KeyError:
            pile[item] = 1

    # Pad to make sure we can generate combinations of the required length
    num_missing = items_per_bin * number_of_bins - sum(pile.values())
    if 0 < num_missing:
        try:
            pile[pad] += num_missing
        except KeyError:
            pile[pad] = num_missing

    # We need this for iteration on possibilities and for ordering the bins
    unique_items = list(sorted(pile.keys()))

    # While each combination is yielded the pile is updated to remove the items in that combination
    def combinations_consuming(size=items_per_bin, items=unique_items):
        if size == 0:
            yield ()
            return
        items = items[:]  # create a new list
        while items:
            item = items[0]
            if pile[item]:
                pile[item] -= 1
                for suffix in combinations_consuming(size - 1, items):
                    yield (item, *suffix)
                pile[item] += 1
            items.pop(0)

    def generate_bins(num=number_of_bins):
        if num == 0:
            yield ()
            return
        for combination in combinations_consuming():
            # The nested call to generate_bins will not be able to use the items already in combination
            for suffix in generate_bins(num - 1):
                yield (combination, *suffix)

    yield from generate_bins()


[print(perm) for perm in permutations_of_items_in_bins([1,2,3],3,3,1)]