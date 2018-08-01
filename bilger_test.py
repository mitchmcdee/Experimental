import random

def main():
    width = 6
    height = 12
    W = range(width)
    H = range(height)

    num_pieces = 6
    board = [[random.randint(0, num_pieces) for w in W] for h in H]
    print(board)

if __name__ == '__main__':
    main()