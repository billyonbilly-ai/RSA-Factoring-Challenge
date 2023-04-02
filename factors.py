import math
import sys

def factorize(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return (i, n//i)
    return None

if len(sys.argv) < 2:
    print("Usage: factors <file>")
    exit(1)

filename = sys.argv[1]

with open(filename) as file:
    for line in file:
        n = int(line.strip())
        factors = factorize(n)
        if factors:
            print(f"{n}={factors[0]}*{factors[1]}")
