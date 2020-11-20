import sys

with open(sys.argv[1]) as inp:
    a = inp.readline()
    b = inp.readline()
print(int(a) + int(b))
