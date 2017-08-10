from hashlib import md5

printOutput = False
comparisonBytes = 5
base = "43596658"

hash = md5(base.encode('utf-8')).hexdigest()[:comparisonBytes]

padding = 0;
print("Starting hashing!")
while (True):
    collisionTest = md5((base + hex(padding)[2:]).encode('utf-8')).hexdigest()[:comparisonBytes]

    if printOutput:
        print("comparing " + hash + " to " + collisionTest)

    if hash == collisionTest:
        print("Found a collision with hash: " + hash)
        break

    padding += 1
