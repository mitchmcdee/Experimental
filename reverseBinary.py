def reverseBits(n):
    print(int(bin(n)[2:].zfill(32)[::-1], 2))

reverseBits(111)