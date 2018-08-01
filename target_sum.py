from operator import mul, truediv, add, sub

def get_options(num_positions, position=0, option=None):
    if option is None:
        option = [add] * (num_positions - 1)
    if position == num_positions - 1:
        return
    for operation in (mul, truediv, add, sub):
        new_option = option[:]
        new_option[position] = operation
        yield new_option
        for next_potion in get_options(num_positions, position + 1, new_option):
            yield next_potion

def get_number_of_ways(target, numbers):
    count = 0
    for option in get_options(len(numbers)):
        result = numbers[0]
        for i, operation in enumerate(option):
            result = operation(result, numbers[i + 1])
        if result == target:
            count += 1
            print(numbers, option) # Shows how it reached target
    return count

def main():
    target = 10
    number = 12345
    numbers = [int(digit) for digit in str(number)]
    print(get_number_of_ways(target, numbers))

if __name__ == '__main__':
    main()
